import os
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from config import Config
from embeddings import embedder

def get_vectorstore(persist_directory: str = None):
    """
    Initialize or connect to an existing Chroma vector store.
    """
    persist_directory = persist_directory or Config.CHROMA_DIR
    os.makedirs(persist_directory, exist_ok=True)

    vectordb = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedder.embedder,  # use HF embedding model
    )
    return vectordb


def add_documents(docs: list[Document]):
    """
    Add a list of LangChain Document objects to the Chroma vector store.
    """
    vectordb = get_vectorstore()
    vectordb.add_documents(docs)
    vectordb.persist()
    print(f"✅ Added {len(docs)} documents to vector store at {Config.CHROMA_DIR}")


def get_retriever():
    """
    Returns a retriever interface to query relevant documents for a user question.
    """
    vectordb = get_vectorstore()
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})  # retrieve top 3 docs
    return retriever


# Quick test
if __name__ == "__main__":
    print("Testing Chroma vectorstore connection...")
    db = get_vectorstore()
    print(f"Vectorstore loaded. Found {db._collection.count()} embeddings.")