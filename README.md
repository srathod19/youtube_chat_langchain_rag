# YouTube RAG Chatbot

A production-structured Retrieval-Augmented Generation (RAG) chatbot built using LangChain, FastAPI, ChromaDB, and OpenAI.

The application loads a YouTube video's transcript, converts it into embeddings, stores them in a vector database, and allows users to ask questions about the video using semantic search + LLM reasoning.

---

# Features

* Load YouTube transcripts
* Chunk large transcript text
* Generate embeddings using OpenAI
* Store embeddings in ChromaDB
* Semantic similarity search
* RAG-based question answering
* FastAPI backend
* Swagger API docs
* Modular production-style architecture

---

# Tech Stack

* Python
* FastAPI
* LangChain
* OpenAI API
* ChromaDB
* YouTube Transcript API
* Uvicorn

---

# Project Structure

```bash
youtube-rag/
│
├── app/
│   ├── api/
│   │   └── routes.py
│   │
│   ├── config/
│   │   └── settings.py
│   │
│   ├── rag/
│   │   ├── loader.py
│   │   ├── chunking.py
│   │   ├── embeddings.py
│   │   ├── vectorstore.py
│   │   ├── retriever.py
│   │   ├── chain.py
│   │   └── prompts.py
│   │
│   └── main.py
│
├── chroma_db/
├── .env
├── requirements.txt
├── run.py
└── README.md
```

---

# How RAG Works

```text
YouTube Video
      ↓
Transcript Extraction
      ↓
Text Chunking
      ↓
Embeddings Creation
      ↓
Store in ChromaDB
      ↓
Semantic Retrieval
      ↓
LLM Generates Final Answer
```

---

# Installation

## 1. Clone Repository

```bash
git clone <your_repo_url>

cd youtube-rag
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv env

.\env\Scripts\Activate.ps1
```

### Mac/Linux

```bash
python3 -m venv env

source env/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory.

```env
OPENAI_API_KEY=your_openai_api_key
```

---

# Run the Application

```bash
uvicorn app.main:app --reload
```

Server runs at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Load YouTube Video

### POST `/load-video`

Loads transcript, chunks text, creates embeddings, and stores them in ChromaDB.

### Example

```json
{
  "video_id": "dQw4w9WgXcQ"
}
```

---

## Ask Question

### POST `/ask`

Ask questions about the loaded YouTube video.

### Example

```json
{
  "question": "What is the main topic of the video?"
}
```

---

# Example Workflow

1. Load a YouTube video
2. Transcript gets embedded into vector database
3. Ask questions about the video
4. RAG pipeline retrieves relevant chunks
5. OpenAI generates grounded answers

---

# Core RAG Components

| Component  | Purpose                 |
| ---------- | ----------------------- |
| Loader     | Fetch transcript        |
| Chunking   | Split large text        |
| Embeddings | Convert text to vectors |
| Vector DB  | Store embeddings        |
| Retriever  | Semantic search         |
| LLM        | Generate final response |

---

# Future Improvements

* Multiple video support
* Persistent collections
* Streaming responses
* Chat memory
* Source citations
* Hybrid search
* Reranking
* Authentication
* Frontend UI
* Docker deployment

---

# Example Use Cases

* Educational video assistant
* Course Q&A chatbot
* Podcast summarizer
* YouTube knowledge assistant
* Internal video documentation search

---

# Learning Goals

This project demonstrates:

* RAG architecture
* Vector databases
* Semantic search
* Embeddings
* LangChain pipelines
* FastAPI backend development

---

# License

MIT License
