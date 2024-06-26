from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

# Criando o Nath
bot = ChatBot('MeuBot')

# treinador do Nath
treinador = ListTrainer(bot)

# Diálogos de treinamento para o Nath
treinador.train([
    'Oi!',
    'Olá, como posso ajudar?',
    'Qual é o seu nome?',
    'Meu nome é Nath. E você?',
    'Me chamo usuário.',
    'Prazer em conhecê-lo, usuário!',
])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-message', methods=['POST'])
def send_message():
    message = request.json['message']
    response = str(bot.get_response(message))
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
