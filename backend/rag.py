import os
import sys
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


def retrieve_context(
    query: str, 
    lang: str = "en", 
    service_id: Optional[int] = None, 
    top_k: int = 8
) -> Tuple[str, List[Dict[str, Any]]]:
    """
    Retrieves top-k context chunks from ChromaDB for the given query.
    Returns:
        Formatted context string, and list of metadata dictionaries.
    """
    # E5 Query format convention requires "query: " prefix
    query_text = f"query: {query}"
    query_vector = embedding_model.encode(query_text).tolist()

    where_clause = {"lang": lang}
    if service_id:
        where_clause = {
            "$and": [
                {"lang": lang},
                {"service_id": int(service_id)}
            ]
        }

    print(f"[RAG] Querying collection '{COLLECTION_NAME}' (lang='{lang}', service_id={service_id}, top_k={top_k})")
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

    # Debug print chunks to console
    if os.getenv("DEBUG_PRINT_CHUNKS", "true").lower() == "true":
        print(f"[RAG] Retrieved {len(top_chunks)} chunks:")
        for idx, chunk in enumerate(top_chunks):
            meta = chunk["metadata"]
            print(f"  Chunk {idx+1}: Service={meta.get('service_id')}, Section={meta.get('section')}, Distance={chunk['distance']:.4f}")
            print(f"  Content: {chunk['text'][:150]}...")

    # Build structured context string with labels
    context_parts = []
    metadata_list = []
    for idx, chunk in enumerate(top_chunks):
        meta = chunk["metadata"]
        doc_type = meta.get("doc_type", "web")
        label = "Official Service Specification Profile" if doc_type == "web" else "User Manual & Guidelines"
        context_parts.append(
            f"--- Source {idx+1}: [{label}] ---\n"
            f"Service: {meta.get('service_name')} (ID: {meta.get('service_id')})\n"
            f"Section: {meta.get('section')}\n"
            f"Content:\n{chunk['text']}\n"
        )
        metadata_list.append(meta)

    context_string = "\n".join(context_parts)
    return context_string, metadata_list
