"""
Script to load local documents, split into chunks,
embed them using Hugging Face, and store in Chroma vector DB.
"""

from ingestion.utils import load_documents, chunk_documents
from vectorstore import add_documents


def ingest_documents(data_dir: str = "./data"):
    """
    Main ingestion pipeline.
    """
    print("🚀 Starting ingestion pipeline...")
    docs = load_documents(data_dir)
    chunks = chunk_documents(docs)
    add_documents(chunks)
    print("✅ Ingestion complete!")


if __name__ == "__main__":
    # Run this script directly to ingest docs from the ./data folder
    ingest_documents()
