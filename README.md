# Customer Support Automation

An AI-powered customer support automation system built using
LangGraph, RAG, vector search, and a ticketing workflow.

## Features

- Ticket classification
- Knowledge-base retrieval using RAG
- AI-generated response suggestions
- Ticket escalation
- LangGraph-based workflow orchestration
- FAISS vector search
- Streamlit user interface
- FastAPI-based ticketing API

## Project Structure

```text
knowledge_base/
ticketing/
app.py
classifier.py
config.py
embeddings.py
ingestion.py
prompts.py
rag.py
response_generator.py
state.py
workflow.py
requirements.txt
tests/
```

## Setup
Clone the repository:
```
git clone <your-repository-url>
cd Customer-Support-Automation
```

Create a virtual environment:
```
python -m venv myvenv
```

Activate it on Windows:
```
.\myvenv\Scripts\Activate 
```

Install dependencies:
```
pip install -r requirements.txt
```

Create .env:
```
GOOGLE_API_KEY=your_google_api_key_here
OPENAI_API_KEY=your_api_key_here
```

## Create Vector Store 
Add the required documents to reate a vector store in "knowledge_base" folder and run:
```
python ingestion.py
```

## Run
Start the application:
```
streamlit run app.py
```

The application will be available locally at:
```
http://localhost:8501
```

## Running the Ticketing API
The project also contains a FastAPI-based mock ticketing service.
Open another terminal,
From the project root, run:
```
uvicorn ticketing.api:app --reload --port 8000
```

The API will be available at:
```
The API will be available at:
```

FastAPI's interactive API documentation can be accessed at:
```
http://localhost:8000/docs
```

## Workflow Graph
The workflow can be represented as:

```
             ┌─────────────┐
             │ Ticket Input│
             └──────┬──────┘
                    │
                    ▼
          ┌───────────────────┐
          │   Classification  │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │  Knowledge Search │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │ Response Generation│
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │ Escalation Check  │
          └───────┬─────┬─────┘
                  │     │
             No   │     │ Yes
                  │     │
                  ▼     ▼
          ┌──────────┐ ┌───────────┐
          │ Response │ │ Escalation│
          └──────────┘ └───────────┘
```