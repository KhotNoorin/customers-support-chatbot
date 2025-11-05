from langchain_huggingface import HuggingFaceEndpointEmbeddings
from config import Config


class Embedder:
    """Wrapper class to generate embeddings using Hugging Face Inference API (new endpoint)."""

    def __init__(self):
        if not Config.HF_API_KEY:
            raise ValueError("Missing Hugging Face API key. Set HF_API_KEY in your .env file.")

        self.model_name = Config.HF_EMBEDDING_MODEL

        # Use new router-based inference endpoint
        self.embedder = HuggingFaceEndpointEmbeddings(
            model=self.model_name,
            huggingfacehub_api_token=Config.HF_API_KEY,
        )

    def embed_text(self, text: str):
        """Generate embedding for a single string."""
        return self.embedder.embed_query(text)

    def embed_documents(self, texts: list[str]):
        """Generate embeddings for multiple documents."""
        return self.embedder.embed_documents(texts)


embedder = Embedder()

if __name__ == "__main__":
    sample = "Testing Hugging Face new endpoint embedding"
    vector = embedder.embed_text(sample)
    print(f"Embedding length: {len(vector)}")
    print(f"First 5 dims: {vector[:5]}")