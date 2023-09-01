from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from keyboard import create_website_button

# Функция для регистрации обработчика события присоединения нового участника к чату
def register_handlers(dp):
    @dp.message_handler(content_types=[types.ContentType.NEW_CHAT_MEMBERS])
    async def on_new_chat_members(message: types.Message):
        for member in message.new_chat_members:
            if not member.is_bot and member.username:
                welcome_message = f"""Добро пожаловать, @{member.username}! 

Мы рады видеть Вас здесь.

Просим Вас ознакомится с информацией о тематике чата и некоторыми правилами, нажав на кнопку ниже
"""

                keyboard = types.InlineKeyboardMarkup()
                website_button = create_website_button()  # Используем функцию из keyboard.py
                keyboard.add(website_button)

                await message.answer(welcome_message, reply_markup=keyboard)