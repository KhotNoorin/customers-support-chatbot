"""
embeddings package
------------------
This package handles text embedding generation for the RAG chatbot.

Usage Example:
    from embeddings import embedder
    vector = embedder.embed_text("Hello world")
"""

from .embedder import embedder, Embedder

__all__ = ["embedder", "Embedder"]
