import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader, UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from config import Config

def load_documents(data_dir: str = "./data"):
    """
    Load supported documents (PDF, TXT, MD) from the data directory.
    Returns a list of LangChain Document objects.
    """
    docs = []
    supported_exts = [".pdf", ".txt", ".md"]

    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Data directory not found: {data_dir}")

    for root, _, files in os.walk(data_dir):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            path = os.path.join(root, file)

            try:
                if ext == ".pdf":
                    loader = PyPDFLoader(path)
                elif ext == ".txt":
                    loader = TextLoader(path, encoding="utf-8")
                elif ext == ".md":
                    loader = UnstructuredMarkdownLoader(path)
                else:
                    continue

                docs.extend(loader.load())
                print(f"📄 Loaded {file}")

            except Exception as e:
                print(f"⚠️ Failed to load {file}: {e}")

    return docs


def chunk_documents(docs: list[Document]):
    """
    Split documents into smaller chunks for embedding.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=Config.INGESTION_CHUNK_SIZE,
        chunk_overlap=Config.INGESTION_CHUNK_OVERLAP,
    )
    chunks = text_splitter.split_documents(docs)
    print(f"✂️ Split into {len(chunks)} text chunks.")
    return chunks