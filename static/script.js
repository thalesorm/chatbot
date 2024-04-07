const chatMessages = document.getElementById("chat-messages");
const userInput = document.getElementById("user-input");

// Função para enviar a mensagem
function sendMessage() {
  const message = userInput.value;
  if (message.trim() === "") return; // Impede o envio de mensagens em branco
  displayMessage("Você", message);
  userInput.value = "";

  // Envie a mensagem para o servidor
  fetch("/send-message", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message }),
  })
    .then((response) => response.json())
    .then((data) => {
      displayMessage("Nath", data.response);
    });
}

// Função para exibir a mensagem na janela de chat
function displayMessage(sender, message) {
  const messageElement = document.createElement("div");
  messageElement.className =
    sender === "Você" ? "sent-message" : "received-message";
  messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
  chatMessages.appendChild(messageElement);
  // Role até o final da janela de chat
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Adicionar evento de teclado ao campo de entrada
userInput.addEventListener("keydown", function (event) {
  if (event.keyCode === 13) {
    // Se a tecla pressionada for "Enter"
    event.preventDefault(); // Impede o comportamento padrão de quebrar linha
    sendMessage(); // Chama a função sendMessage para enviar a mensagem
  }
});

// Exibir uma mensagem de boas-vindas do ChatBot quando a página é carregada
window.onload = () => {
  displayMessage("Nath", "Olá! Como posso ajudar?");
};
