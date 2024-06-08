import telebot

token = "7319327247:AAEo-Fxmd8yOraX38cwTWRkGs5c6PeRkjaM"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'hello'])
def hello(message):
    bot.send_message(message.chat.id, message.chat.username)


bot.infinity_polling()
