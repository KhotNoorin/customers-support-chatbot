# Customer Support Chatbot

A Python-based customer support chatbot leveraging **LangChain**, **HuggingFace**, and **Chroma** for natural language understanding and retrieval-based responses. This project allows you to build a virtual assistant that can interact with customers, answer questions, and provide intelligent responses.

---

## 🚀 Features

- Retrieval-based question answering using LangChain.
- Integration with HuggingFace models for NLP.
- Chroma database for storing and querying embeddings.
- Modular and extendable architecture.
- Easy setup with a virtual environment.

---

## 📦 Project Structure

rag-flask-chatbot/

├─ .env                      # local env vars (HF_API_KEY, CHROMA_DIR, etc.)

├─ README.md

├─ requirements.txt

├─ app.py                    # Flask app (web UI + API endpoints)

├─ config.py                 # configuration & env var loading

├─ ingestion/

│  ├─ __init__.py

│  ├─ ingest.py              # script to load local docs and create/update vector DB

│  └─ utils.py               # helpers: file loaders, text splitters

├─ embeddings/

│  ├─ __init__.py

│  ├─ embedder.py            # wrapper to call Hugging Face embeddings via API

├─ vectorstore/

│  ├─ __init__.py

│  ├─ store.py               # create/connect to Chroma vectorstore + persist

├─ rag/

│  ├─ __init__.py

│  ├─ rag_chain.py           # assemble LangChain Retriever + LLM (RAG chain)

├─ templates/

│  └─ index.html             # simple chat UI (Bootstrap)

├─ static/

│  ├─ css/

│  │  └─ styles.css

│  └─ js/

│     └─ chat.js             # frontend JS to call Flask endpoints   

└─ data/ 

## 🧑‍💻 Author

Noorin Nasir Khot
