"""
vectorstore package
-------------------
Handles creation, connection, and retrieval operations
for the Chroma vector database used in the RAG pipeline.
"""

from .store import get_vectorstore, add_documents, get_retriever

__all__ = ["get_vectorstore", "add_documents", "get_retriever"]
