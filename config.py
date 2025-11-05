import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

class Config:
    """Central configuration class for the RAG Flask Chatbot."""

    # ---- Flask ----
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "supersecretkey")
    PORT = int(os.getenv("PORT", 5000))

    # ---- Hugging Face ----
    HF_API_KEY = os.getenv("HF_API_KEY")
    HF_MODEL = os.getenv("HF_MODEL", "mistralai/Mistral-7B-Instruct-v0.2")
    HF_EMBEDDING_MODEL = os.getenv(
        "HF_EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2"
    )

    # ---- Vector Store ----
    CHROMA_DIR = os.getenv("CHROMA_DIR", "./chroma_db")

    # ---- Ingestion ----
    INGESTION_CHUNK_SIZE = int(os.getenv("INGESTION_CHUNK_SIZE", 1000))
    INGESTION_CHUNK_OVERLAP = int(os.getenv("INGESTION_CHUNK_OVERLAP", 200))

    # ---- Logging ----
    LOG_DIR = os.getenv("LOG_DIR", "./logs")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    # ---- Validation ----
    @staticmethod
    def validate():
        """Check that critical environment variables are set."""
        missing = []
        if not Config.HF_API_KEY:
            missing.append("HF_API_KEY")
        if missing:
            raise EnvironmentError(f"Missing required environment vars: {', '.join(missing)}")

# Create logs directory if it doesn’t exist
os.makedirs(Config.LOG_DIR, exist_ok=True)