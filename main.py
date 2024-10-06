from aiogram import Bot, Dispatcher, executor
from bot.handlers import register_handlers
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Register bot handlers
register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp)
