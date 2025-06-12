import os
from dotenv import load_dotenv

load_dotenv('Telegram/data/.env')
API_TOKEN = os.getenv("API_TELEGRAM")
ADMINS = os.getenv("ADMINS")
PASSWORD = os.getenv("PASSWORD")

BUTTONS = {
    'adjust': 1,
    'buttons': ['Ежедневные задания', 'Статистика', 'Перейти на сайт', 'Выйти']
}

BUTTONS_ADMIN = {
    'adjust': 1,
    'buttons': ['Сделать рассылку', 'Вернуться']
}

ADMIN_BTN = ['⚙️АДМИН ПАНЕЛЬ⚙️']

start_message = """👋 Добро пожаловать в Sportly Bot!

Здесь ты можешь:
🔹 Получать напоминания о тренировках
🔹 Узнавать свои ежедневные задания
🔹 Следить за прогрессом даже без входа в приложение

🔐 Чтобы начать использовать все возможности бота, тебе нужно войти в свой аккаунт на Sportly .
Нажми кнопку ниже:"""

start_message_logged = """👋 Добро пожаловать в Sportly Bot!

Здесь ты можешь:
🔹 Получать напоминания о тренировках
🔹 Узнавать свои ежедневные задания
🔹 Следить за прогрессом даже без входа в приложение

Вы уже вошли в аккаунт под именем """


from aiogram.fsm.state import StatesGroup, State


class Logging(StatesGroup):
    email = State()
    password = State()


SMILES = {
    True: '✅',
    False: '❌',
}