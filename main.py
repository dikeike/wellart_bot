import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.utils import executor

from config import TOKEN
from handlers.start import register_start_handlers
from handlers.generate import register_generate_handlers
from handlers.modify import register_modify_handlers
from handlers.admin import register_admin_handlers

# -----------------------------------------------------
# Логирование
# -----------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# -----------------------------------------------------
# Инициализация бота
# -----------------------------------------------------
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# -----------------------------------------------------
# Регистрация хендлеров
# -----------------------------------------------------
register_start_handlers(dp)
register_generate_handlers(dp)
register_modify_handlers(dp)
register_admin_handlers(dp)

# -----------------------------------------------------
# Ping-команда для проверки
# -----------------------------------------------------
@dp.message_handler(commands=["ping"])
async def ping(message: Message):
    await message.answer("Bot is running ✔️")

# -----------------------------------------------------
# Старт бота
# -----------------------------------------------------
if __name__ == "__main__":
    logger.info("bot started...")
    executor.start_polling(dp, skip_updates=True)