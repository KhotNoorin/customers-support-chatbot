const chatbox = document.getElementById("chatbox");
const input = document.getElementById("user-input");
const button = document.getElementById("send-btn");

function addMessage(content, sender) {
    const msgDiv = document.createElement("div");
    msgDiv.className = "message " + sender;

    const timestamp = new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
    msgDiv.innerHTML = `${content}<div class="timestamp">${timestamp}</div>`;

    chatbox.appendChild(msgDiv);
    chatbox.scrollTop = chatbox.scrollHeight; // auto-scroll
}

async function sendMessage() {
    const question = input.value.trim();
    if (!question) return;

    addMessage("You: " + question, "user");
    input.value = "";

    // Send query to Flask backend
    try {
        const response = await fetch("/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question })
        });

        const data = await response.json();
        addMessage("Bot: " + (data.answer || data.error), "bot");

    } catch (err) {
        addMessage("Bot: Error connecting to server.", "bot");
    }
}

button.addEventListener("click", sendMessage);
input.addEventListener("keydown", (e) => { if (e.key === "Enter") sendMessage(); });