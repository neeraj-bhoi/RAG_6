import os
import sys
import re
from typing import List, Dict, Any, Tuple, Optional
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import chromadb

# Ensure stdout uses UTF-8 to prevent Windows print crash
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()

# Configuration paths
WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "./chroma_db")
EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL", "intfloat/multilingual-e5-large")
COLLECTION_NAME = "sewa_setu_services"

# Initialize models & client on import
print(f"[RAG] Loading embedding model: {EMBEDDING_MODEL_NAME}...")
embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME)

print(f"[RAG] Connecting to ChromaDB at: {CHROMA_DB_PATH}")
chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
collection = chroma_client.get_collection(COLLECTION_NAME)
print(f"[RAG] Connected successfully to collection '{COLLECTION_NAME}' (Total count: {collection.count()})")


def tokenize_text(text: str) -> set:
    """
    Preserves both standard word characters and Devanagari script characters (including combining marks).
    """
    cleaned = re.sub(r'[^\w\u0900-\u097f\s]', ' ', text.lower())
    return set(cleaned.split())


def rerank_chunks(
    query: str, 
    chunks: List[Dict[str, Any]], 
    top_n: int = 4,
    english_query: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Reranks the retrieved chunks using a hybrid semantic distance + lexical overlap score.
    Returns:
        The top_n reranked chunks.
    """
    stop_words = {
        'a', 'an', 'the', 'for', 'to', 'is', 'of', 'in', 'on', 'at', 'by', 'with', 'from', 'what', 'which', 'who', 'how', 'why', 'where', 'when',
        'के', 'लिए', 'है', 'का', 'की', 'में', 'को', 'और', 'से', 'पर', 'हो', 'कर', 'था', 'थी', 'थे', 'या', 'भी', 'ने', 'तक', 'जो', 'तो', 'ही'
    }

    # Pre-tokenize original Hindi query keywords
    hi_words = tokenize_text(query)
    hi_keywords = hi_words - stop_words
    if not hi_keywords:
        hi_keywords = hi_words

    # Pre-tokenize English query keywords
    en_query_to_use = english_query if english_query else query
    en_words = tokenize_text(en_query_to_use)
    en_keywords = en_words - stop_words
    if not en_keywords:
        en_keywords = en_words

    scored_chunks = []
    for chunk in chunks:
        # Convert distance to semantic similarity (smaller distance -> higher similarity)
        distance = chunk.get("distance", 1.0)
        semantic_sim = max(0.0, 1.0 - (distance / 2.0))

        # Lexical keyword overlap score based on chunk language
        chunk_lang = chunk["metadata"].get("lang", "en")
        chunk_words = tokenize_text(chunk["text"])

        if chunk_lang == "hi":
            # Match against original Hindi query keywords
            overlap = len(hi_keywords.intersection(chunk_words))
            lexical_score = overlap / len(hi_keywords) if hi_keywords else 0.0
        else:
            # Match against English/translated query keywords
            overlap = len(en_keywords.intersection(chunk_words))
            lexical_score = overlap / len(en_keywords) if en_keywords else 0.0

        # Combine scores (semantic similarity weighted at 0.7, lexical overlap at 0.3)
        hybrid_score = 0.7 * semantic_sim + 0.3 * lexical_score
        chunk["hybrid_score"] = hybrid_score
        scored_chunks.append(chunk)

    # Sort chunks by hybrid score descending
    scored_chunks.sort(key=lambda x: x["hybrid_score"], reverse=True)
    
    if os.getenv("DEBUG_PRINT_CHUNKS", "true").lower() == "true":
        print(f"[RAG Reranking] Reranked {len(scored_chunks)} chunks:")
        for idx, chunk in enumerate(scored_chunks):
            meta = chunk["metadata"]
            print(f"  Rank {idx+1}: Service={meta.get('service_id')}, Section={meta.get('section')}, Lang={meta.get('lang')}, Distance={chunk.get('distance'):.4f}, HybridScore={chunk['hybrid_score']:.4f}")
    
    return scored_chunks[:top_n]


def retrieve_context(
    query: str, 
    service_id: Optional[int] = None, 
    top_k: int = 6,
    english_query: Optional[str] = None
) -> Tuple[str, List[Dict[str, Any]]]:
    """
    Retrieves top_k language-agnostic chunks from ChromaDB, reranks them, 
    and returns a structured context string from the top 4 chunks.
    """
    # Increase retrieve size if no specific service filter is specified
    if service_id is None:
        top_k = max(top_k, 15)

    # Use english_query if available for embedding search prefix
    search_query = english_query if english_query else query
    query_text = f"query: {search_query}"
    query_vector = embedding_model.encode(query_text).tolist()

    where_clause = None
    if service_id:
        where_clause = {"service_id": int(service_id)}

    print(f"[RAG] Querying database (service_id={service_id}, top_k={top_k}, search_query='{search_query}')")
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=top_k,
        where=where_clause
    )

    top_chunks = []
    if results and "documents" in results and results["documents"]:
        docs = results["documents"][0]
        metas = results["metadatas"][0]
        distances = results["distances"][0]
        for idx, (doc, meta) in enumerate(zip(docs, metas)):
            top_chunks.append({
                "text": doc, 
                "metadata": meta, 
                "distance": distances[idx]
            })

    # Rerank the 6 chunks to select the top 4
    top_4_chunks = rerank_chunks(query, top_chunks, top_n=4, english_query=english_query)

    # Build structured context string with labels
    context_parts = []
    metadata_list = []
    for idx, chunk in enumerate(top_4_chunks):
        meta = chunk["metadata"]
        doc_type = meta.get("doc_type", "web")
        lang_label = "English" if meta.get("lang") == "en" else "Hindi"
        label = f"Official Specification ({lang_label})" if doc_type == "web" else f"User Manual ({lang_label})"
        context_parts.append(
            f"--- Source {idx+1}: [{label}] ---\n"
            f"Service: {meta.get('service_name')} (ID: {meta.get('service_id')})\n"
            f"Section: {meta.get('section')}\n"
            f"Content:\n{chunk['text']}\n"
        )
        metadata_list.append(meta)

    context_string = "\n".join(context_parts)
    return context_string, metadata_list
