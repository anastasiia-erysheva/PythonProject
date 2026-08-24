import os
import telebot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print("Получена команда /start!")
    bot.reply_to(message, "Привет! Я твой первый рабочий бот. Мы это сделали!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(f"Новое сообщение: {message.text}")
    bot.reply_to(message, f"Ты написала: {message.text}")

print("--- БОТ ЗАПУЩЕН И ЖДЕТ СООБЩЕНИЙ ---")
bot.infinity_polling()