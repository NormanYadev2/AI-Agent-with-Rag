# Restaurant Review Chatbot with RAG and Agent

This project implements a Retrieval-Augmented Generation (RAG) chatbot that answers questions about a pizza restaurant based on real customer reviews. It leverages LangChain, Ollama LLMs, and a Chroma vector database to deliver relevant and context-aware responses.

## Features

- Uses **ChromaDB** to store and semantically search restaurant reviews.
- Uses **Ollama LLM** (`llama3.2`) for natural language understanding and generation.
- Wraps the retriever as a **tool** accessible to a LangChain **agent**.
- Agent dynamically decides when and how to use the retriever to answer questions.
- Interactive command-line interface for asking questions.

## Project Structure

- `vector.py` — Loads review data, generates embeddings with Ollama, and builds the vector store retriever.
- `tools.py` — Defines the retriever as a tool for the agent.
- `main.py` — Runs the agent-based chatbot CLI loop.


### Prerequisites

- Python 3.8+
- Ollama installed with models:
  - `llama3.2`
  - `mxbai-embed-large`



