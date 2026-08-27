import os
import random
import telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

lessons_a2 = [
    {
        "id": 1,
        "topic": "Прошедшее определенное время (-dı / -di / -du / -dü)",
        "rule": "Используется для действий в прошлом, свидетелем которых вы были лично.",
        "examples": [
            "Bugün markete gittim. — Сегодня я сходила в магазин.",
            "Kahve içtik. — Мы выпили кофе.",
            "Otobüs geldi. — Автобус приехал."
        ],
        "task": "Как перевести на турецкий: «Я купила хлеб»? (ekmek — хлеб, almak — покупать)"
    },
    {
        "id": 2,
        "topic": "Деепричастие -ıp / -ip / -up / -üp",
        "rule": "Соединяет два последовательных действия в одно предложение («сделав X, сделал Y»).",
        "examples": [
            "Marketten ekmek alıp eve döndüm. — Купив в магазине хлеб, я вернулась домой.",
            "Kahvaltı yapıp işe gittim. — Позавтракав, я пошла на работу."
        ],
        "task": "Соедини два действия с помощью -ıp: «Ders çalıştım» (позанималась) и «uyudum» (поспала)."
    },
    {
        "id": 3,
        "topic": "Конструкция -dığı zaman / -diği zaman (Когда...)",
        "rule": "Обозначает время совершения действия («когда я делаю / когда я сделала...»).",
        "examples": [
            "Eve geldiğim zaman seni arayacağım. — Когда я приду домой, я тебе позвоню.",
            "Yağmur yağdığı zaman evde kalırım. — Когда идет дождь, я остаюсь дома."
        ],
        "task": "Составь выражение: «Когда я читаю книгу...» (kitap okumak)."
    },
    {
        "id": 4,
        "topic": "Долженствование -malı / -meli (Должен / Нужно)",
        "rule": "Показывает обязанность или настоятельный совет что-то сделать.",
        "examples": [
            "Bugün dinlenmeliyim. — Сегодня я должна отдохнуть.",
            "Daha fazla su içmelisin. — Ты должен пить больше воды."
        ],
        "task": "Переведи на турецкий: «Я должна позаниматься» (ders çalışmak)."
    },
    {
        "id": 5,
        "topic": "Цель действия -maya / -meye (Чтобы / Для того чтобы)",
        "rule": "Дательный падеж с инфинитивом показывает цель отправления куда-то («пошел, чтобы сделать...»).",
        "examples": [
            "Ekmek almaya gittim. — Я пошел (за чем? / чтобы что сделать?) купить хлеб.",
            "Türkçe öğrenmeye çalışıyorum. — Я стараюсь (что делать?) учить турецкий."
        ],
        "task": "Составь фразу: «Я пошла гулять» (пошла — gittim, гулять — yürüyüş yapmak)."
    }
]
def get_main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_lesson = types.KeyboardButton("📘 Урок дня (A2)")
    keyboard.add(btn_lesson)
    return keyboard


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "Merhaba! Я твой помощник по турецкому языку (A2) и Python!\n\n"
        "Нажимай кнопку «Урок дня (A2)», чтобы изучать грамматику и разбирать примеры."
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=get_main_keyboard())


@bot.message_handler(func=lambda message: message.text == "📘 Урок дня (A2)" or message.text == "/lesson")
def send_lesson(message):
    lesson = random.choice(lessons_a2)

    examples_text = "\n".join([f"• {ex}" for ex in lesson['examples']])

    response = (
        f"📌 *Урок: {lesson['topic']}*\n\n"
        f"💡 *Правило:* {lesson['rule']}\n\n"
        f"📝 *Примеры из жизни:*\n{examples_text}\n\n"
        f"🎯 *Практика:* {lesson['task']}"
    )

    bot.send_message(message.chat.id, response, parse_mode="Markdown", reply_markup=get_main_keyboard())


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Принято! Напиши свой вариант ответа на задание или нажми «📘 Урок дня (A2)».")


print("--- БОТ ЗАПУЩЕН И ЖДЕТ СООБЩЕНИЙ ---")
bot.infinity_polling()