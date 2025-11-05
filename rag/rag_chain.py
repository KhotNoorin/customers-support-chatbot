import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
if not HUGGINGFACE_API_KEY:
    raise ValueError("❌ Missing Hugging Face API key. Please set it in your .env file.")


# Imports for chain and vectorstore
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEndpoint


from embeddings.embedder import embedder  # your custom embedder

def build_rag_chain(persist_dir: str = "./chroma_db"):
    """
    Build the RAG (Retrieval‑Augmented Generation) pipeline.
    """
    # 1. Connect or create the vector store
    vectordb = Chroma(
        persist_directory=persist_dir,
        embedding_function=embedder.embedder
    )

    # 2. Create the retriever
    retriever = vectordb.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    # 3. Set up the LLM using Hugging Face endpoint
    llm = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.3",
        temperature=0.3,
        max_new_tokens=512,
        huggingfacehub_api_token=HUGGINGFACE_API_KEY
    )

    # 4. Build the RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",             # simplest strategy
        return_source_documents=True
    )

    print("✅ RAG Chain successfully built!")
    return qa_chain

def ask_question(query: str, chain=None):
    """
    Run a query through the RAG pipeline and get an answer.
    """
    if chain is None:
        chain = build_rag_chain()

    result = chain.invoke({"query": query})
    answer = result["result"]

    print("\n🔍 Question:", query)
    print("💬 Answer:", answer)

    if "source_documents" in result:
        print("\n📚 Sources:")
        for doc in result["source_documents"]:
            print("-", doc.metadata.get("source", "Unknown"))

    return answer

if __name__ == "__main__":
    qa = build_rag_chain()
    while True:
        user_q = input("\n🧠 Ask something (or type 'exit'): ")
        if user_q.lower() in ["exit", "quit"]:
            break
        ask_question(user_q, qa)