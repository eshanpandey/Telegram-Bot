import os
from dotenv import load_dotenv
import telebot

load_dotenv()  
BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'Hello'])
def send_greetings(message):
    bot.reply_to(message, "Hi How are you today?")
    

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    


bot.infinity_polling()
