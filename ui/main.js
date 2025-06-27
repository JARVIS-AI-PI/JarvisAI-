// 📁 JarvisAI/ui/main.js

function sendCommand() {
    const input = document.getElementById("input").value;
    fetch("/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ prompt: input })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").innerText = data.response;
        document.getElementById("input").value = "";
    });
}
