# import telebot

# bot = telebot.TeleBot("TOKEN")

# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, "Bot ishlayapti!")

# bot.polling()
import telebot

TOKEN = "BOT_TOKEN_INGIZ"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Men 24/7 ishlayman.")

bot.infinity_polling()  # Bu botni doimiy ishlashga qo'yadi
