# Autonomous Research Agent

An advanced **multi-agent AI system** that autonomously performs web research, analyzes information, and generates structured reports using **LangGraph orchestration, Retrieval-Augmented Generation (RAG), and local LLMs**.

---

## Overview

This project simulates how real-world AI research assistants (like Perplexity / Deep Research systems) work.

It takes a user query and:

* Plans the research
* Searches the web
* Scrapes articles
* Stores knowledge in a vector database
* Retrieves relevant information
* Analyzes content
* Generates a structured research report

All using a **multi-agent workflow with decision-making loops**.

---

## Architecture

```
User Query
   ↓
LangGraph Orchestrator
   ↓
Planner Agent
   ↓
Research Agent
   ↓
Web Search (DuckDuckGo)
   ↓
Web Scraper (Newspaper3k)
   ↓
Vector Database (Chroma)
   ↓
Retriever (Vector Search + Metadata Filtering)
   ↓
Analysis Agent
   ↓
Decision Node
   ├── Research again (if insufficient info)
   └── Writer Agent
           ↓
     Final Report
```

---

## Key Features

* 1. **Multi-Agent Workflow** using LangGraph
* 2. **Autonomous Decision Making** (loop until sufficient info)
* 3. **Retrieval-Augmented Generation (RAG)**
* 4. **Vector Search + Metadata Filtering**
* 5. **Live Web Search & Scraping**
* 6. **Local LLM (Ollama - Llama3.1)**
* 7. **Chroma Vector Database**
* 8. **Modular Agent-Based Design**
* 9. **Full-stack integration (FastAPI + Streamlit)**

---

## Tech Stack

### Core

* Python
* LangGraph
* LangChain

### LLM & Embeddings

* Ollama (Local LLM - Llama3.1)
* nomic-embed-text (Embeddings)

### Backend

* FastAPI

### Frontend

* Streamlit

### Retrieval & Storage

* Chroma Vector Database
* Metadata-based Retrieval

### Tools

* DuckDuckGo Search (ddgs)
* Newspaper3k (Web Scraping)

---

## Project Structure

```
app/
 ├── agents/
 │    ├── planner_agent.py
 │    ├── research_agent.py
 │    ├── analysis_agent.py
 │    └── writer_agent.py
 │
 ├── graph/
 │    └── research_graph.py
 │
 ├── tools/
 │    ├── web_search.py
 │    ├── web_scrapper.py
 │    └── vector_store.py
 │
 ├── memory/
 │    └── state.py
 │
 ├── schemas/
 │    └── report_schema.py
 │
 └── main.py

frontend/
 └── streamlit_app.py

requirements.txt
README.md
```

---

##  Installation

### 1️ Clone the Repository

```bash
git clone https://github.com/yourusername/autonomous-research-agent.git
cd autonomous-research-agent
```

---

### 2️ Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

**Windows:**

```bash
.venv\Scripts\activate
```

**Mac/Linux:**

```bash
source .venv/bin/activate
```

---

### 3️ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️ Install Ollama (Local LLM)

Download from: https://ollama.com

Then pull required models:

```bash
ollama pull llama3.1
ollama pull nomic-embed-text
```

Run Ollama:

```bash
ollama serve
```

---

##  Running the Project

### Start Backend (FastAPI)

```bash
uvicorn app.main:app --reload
```

API Docs:

```
http://127.0.0.1:8000/docs
```

---

### Start Frontend (Streamlit)

```bash
streamlit run frontend/streamlit_app.py
```

---

##  API Endpoints

### POST `/research`

Generate a research report.

#### Example Request:

```
http://127.0.0.1:8000/research?query=What are small language models?
```

#### Response:

```json
{
  "query": "...",
  "report": "Structured research report..."
}
```

---

## State Management (LangGraph)

The system uses a shared state passed across agents:

```python
{
  "query": str,
  "search_queries": List[str],
  "sources": List[str],
  "documents": List[Dict],
  "analysis": str,
  "report": str
}
```

Each agent updates this state during execution.

---

## LangGraph Workflow

* Nodes:

  * Planner
  * Research
  * Scraper + Storage
  * Analysis
  * Writer

* Conditional Flow:

  * If insufficient data → Re-search
  * Else → Generate report

---

## Retrieval System

* Document Chunking (RecursiveCharacterTextSplitter)
* Embeddings (Ollama)
* Vector Storage (Chroma)
* Retrieval:

  * Semantic similarity search
  * Metadata filtering (`url`, `source`)

---

## Example Query

```
What are the latest small language models in 2025?
```

The system will:

1. Plan search queries
2. Fetch web results
3. Scrape content
4. Store embeddings
5. Retrieve relevant chunks
6. Analyze information
7. Generate final report

---

## Acknowledgements

Inspired by modern AI systems like:

* Perplexity AI
* OpenAI Deep Research
* LangGraph Agent Workflows

---

## Author

Divya Kumar Jha
GitHub: https://github.com/DivyaKumarJha
