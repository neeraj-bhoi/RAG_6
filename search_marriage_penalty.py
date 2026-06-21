import os
import sys
import chromadb
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

load_dotenv()

CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "./chroma_db")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "intfloat/multilingual-e5-large")
COLLECTION_NAME = "sewa_setu_services"

client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
collection = client.get_collection(COLLECTION_NAME)

print("Connected to ChromaDB. Fetching all chunks for Service 3...")

# We can query all chunks for service_id = 3
results = collection.get(
    where={"service_id": 3}
)

docs = results["documents"]
metas = results["metadatas"]
print(f"Total chunks found for Service 3: {len(docs)}")

# Let's search for keywords in the chunks
keywords = ["month", "day", "delay", "penalty", "fee", "shadi", "regist", "शुल्क", "विलंब", "महीने", "दिन", "शादी"]

for idx, (doc, meta) in enumerate(zip(docs, metas)):
    doc_lower = doc.lower()
    matches = [k for k in keywords if k in doc_lower]
    if matches:
        print(f"\n--- Chunk {idx+1} | Lang: {meta.get('lang')} | Section: {meta.get('section')} ---")
        print(f"Matches: {matches}")
        print(doc[:400] + "...")
