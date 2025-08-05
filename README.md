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

## System Flow

1. **User Input:** The user types a question about the pizza restaurant (e.g., "What do customers think about the cheese?").
2. **Agent Reasoning:** The LangChain agent (powered by Ollama LLM) receives the question and decides how to answer it.
3. **Tool Invocation:** If needed, the agent calls the **retriever tool**, sending a relevant query to fetch customer reviews from the vector database.
4. **Retrieval:** The retriever performs a semantic search on the stored reviews in Chroma and returns the top relevant documents.
5. **Answer Generation:** The agent processes the retrieved reviews, combines them with its language capabilities, and formulates a coherent answer.
6. **Response Output:** The generated answer is displayed back to the user in the command-line interface.
7. **Repeat:** The loop continues until the user types `q` to quit.



### Prerequisites

- Python 3.8+
- Ollama installed with models:
  - `llama3.2`
  - `mxbai-embed-large`

