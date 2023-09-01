import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware

import config
from handlers import register_handlers
from keyboard import create_website_button

# Настройка уровня логирования и формата сообщений
logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# Инициализация бота и диспетчера
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Регистрация обработчиков
register_handlers(dp)

if __name__ == '__main__':
    from aiogram import executor
    print("ОК")
    executor.start_polling(dp, skip_updates=True)
