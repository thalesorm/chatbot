# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer

# # Crie um ChatBot
# bot = ChatBot('MeuBot')

# # Crie um treinador para o bot
# treinador = ListTrainer(bot)

# # Treine o bot com algumas conversas
# treinador.train([
#     'Oi!',
#     'Olá, como posso ajudar?',
#     'Qual é o seu nome?',
#     'Meu nome é Nath. E você?',
#     'Me chamo usuário.',
#     'Prazer em conhecê-lo, usuário!',
# ])

# # Inicie uma conversa
# print("Olá! Sou a Nath. Você pode começar a conversar comigo. Digite 'sair' quando quiser para encerrarmos.")
# while True:
#     # Obtenha a entrada do usuário
#     entrada = input("Você: ")
#     # Saia do loop se o usuário digitar 'sair'
#     if entrada.lower() == 'sair':
#         print("Até logo!")
#         break
#     # Obtenha a resposta do bot
#     resposta = bot.get_response(entrada)
#     print('Bot:', resposta)
