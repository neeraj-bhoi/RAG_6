# SewaSetu RAG System: Retrieval Process Flow

This document details the exact process flow used by the SewaSetu RAG chatbot backend to resolve user queries, explain how chunks are retrieved, and identify when the vector store vs. direct file resources are accessed.

---

## Architecture Overview

The backend uses a hybrid storage and retrieval approach designed to avoid chunk truncation and ensure the LLM receives complete context for selected services:

*   **ChromaDB Vector Store**: Used for storing document metadata chunks, indexing compiled manuals, and performing cross-lingual/semantic similarity search.
*   **Local File System Cache**: Houses the original JSON profiles under `data/profiles/` and compiled manual text files (which merge parsed web data + extracted PDF contents) under `data/extracted_text/`.
*   **Context Budgets**: Prompts are constrained to a maximum context budget of **25,000 characters** to ensure fast LLM responses and avoid prompt overflow.

---

## Ingestion Pipeline Flow

Before queries are processed, data must be structured and indexed:

```mermaid
graph TD
    A[Scraped HTML + PDF Text] --> B[Generate combined_manual_SID_LANG.txt]
    A --> C[Generate service_SID_LANG.json Profile]
    C --> D[Convert Profile to MD Document]
    D --> E[Store full Profile MD in ChromaDB under ID: meta_SNo_LANG_0]
    B --> F[Chunk Manual into 1500-char segments]
    F --> G[Generate Multilingual MiniLM Embeddings]
    G --> H[Index Manual chunks in ChromaDB under IDs: manual_SNo_LANG_Idx]
```

---

## Query Scenarios & Retrieval Flows

When a request is made to `/api/chat` or `/api/search`, the system routes context retrieval through three main scenarios:

### Scenario A: Scoped Chat Query (`selected_sno` is Passed)

This scenario is triggered when the user explicitly selects a service from the dropdown in the UI. 

```mermaid
sequenceDiagram
    participant UI as Client / UI
    participant API as backend/main.py
    participant DB as ChromaDB (Vector Store)
    participant FS as Local Filesystem (disk)
    participant LLM as LLM (Sarvam AI / Ollama)
    
    UI->>API: POST /api/chat { query, selected_sno: "5", language: "en" }
    Note over API: selected_sno is present.<br/>Target scope is fixed to Domicile (SNo 5).
    API->>DB: collection.get(ids=["meta_5_en_0"])
    DB-->>API: Full structured Profile MD document
    API->>FS: Load data/extracted_text/combined_manual_7_en.txt
    FS-->>API: Full compiled manual text (includes citizenCharter PDF text)
    Note over API: Compile retrieved texts into prompt<br/>(budget-limited to 25k chars)
    API->>LLM: Send system prompt + user query
    LLM-->>API: Generated answer
    API->>UI: Response JSON { response: answer_text }
```

*   **Vector DB Usage**: ChromaDB is queried directly by exact ID (`meta_5_en_0`) using `collection.get()`. Semantic vector similarity search is **bypassed** since the service context scope is explicitly defined.
*   **Other Resources**: The full compiled manual (including its embedded SLA details text) is loaded directly from disk.

---

### Scenario B: Global Chat Query (`selected_sno` is Null)

This scenario is triggered when the user asks a question globally without choosing a service category.

```mermaid
sequenceDiagram
    participant UI as Client / UI
    participant API as backend/main.py
    participant DB as ChromaDB (Vector Store)
    participant FS as Local Filesystem (disk)
    participant LLM as LLM (Sarvam AI / Ollama)
    
    UI->>API: POST /api/chat { query, selected_sno: null, language: "en" }
    Note over API: selected_sno is missing.<br/>Perform semantic lookup.
    API->>DB: collection.query(query_embeddings, n_results=3)
    DB-->>API: Top 3 matching manual/meta chunks + metadata (sno, type)
    Note over API: Extract unique SNos from retrieved metadata.<br/>Example matches SNo "5" (Domicile).
    API->>DB: collection.get(ids=["meta_5_en_0"])
    DB-->>API: Full structured Profile MD document
    API->>FS: Load data/extracted_text/combined_manual_7_en.txt
    FS-->>API: Full compiled manual text
    Note over API: Compile matched service texts into prompt<br/>(budget-limited to 25k chars)
    API->>LLM: Send system prompt + user query
    LLM-->>API: Generated answer
    API->>UI: Response JSON { response: answer_text }
```

*   **Vector DB Usage**: ChromaDB is queried using the query's vector embedding. The top 3 matching chunks are retrieved. The system extracts their `sno` metadata to identify which services are relevant. It then fetches the full metadata document for each matching service.
*   **Other Resources**: For each matched service `sno`, the full compiled manual text file is loaded from disk.

---

### Scenario C: Service Classification / Search (`/api/search`)

This endpoint is used when the frontend needs to map a user's free-text search query (in English, Hindi, or Hinglish) to the correct dropdown serial number (`sno`).

```mermaid
sequenceDiagram
    participant UI as Client / UI
    participant API as backend/main.py
    participant FS as Local Filesystem (disk)
    participant LLM as LLM (Sarvam AI / Ollama)
    
    UI->>API: POST /api/search { query: "shadi praman" }
    API->>FS: Load processed_data/rag_kb_manifest.json
    FS-->>API: List of 9 service metadata objects
    Note over API: Construct service description catalog listing<br/>all SNos, English & Hindi names.
    API->>LLM: Query LLM with service list + classify instructions
    LLM-->>API: JSON output: { "sno": "1", "service_id": "3" }
    API->>UI: Response JSON { "sno": "1", "service_id": "3" }
```

*   **Vector DB Usage**: The vector database is **not accessed** at all for this scenario.
*   **Other Resources**: The backend reads `rag_kb_manifest.json` on disk to load the catalog mapping and embeds the entire catalog as a text block inside the system classification prompt.
