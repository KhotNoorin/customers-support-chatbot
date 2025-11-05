from flask import Flask, render_template, request, jsonify
from rag.rag_chain import build_rag_chain, ask_question

# =========================
# Initialize Flask app
# =========================
app = Flask(__name__)

# Build RAG chain once at startup
qa_chain = build_rag_chain()


# =========================
# Routes
# =========================
@app.route("/")
def home():
    """Render home page with chat interface."""
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    """Receive user query and return chatbot response."""
    data = request.json
    user_question = data.get("question", "").strip()

    if not user_question:
        return jsonify({"error": "No question provided"}), 400

    # Get answer from RAG chain
    answer = ask_question(user_question, chain=qa_chain)
    return jsonify({"answer": answer})


# =========================
# Run Flask app
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)