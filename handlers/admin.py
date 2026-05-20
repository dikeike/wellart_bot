from aiogram import Dispatcher
from aiogram.types import Message
from config import NSFW_ENABLED
import os

# -----------------------------------------------------
# ID админа (твой Telegram ID — позже подставим)
# -----------------------------------------------------
ADMIN_ID = 0  # ← сюда впишем твой ID, когда ты скажешь

# -----------------------------------------------------
# Команда включения NSFW
# -----------------------------------------------------
async def enable_nsfw(message: Message):
    if message.from_user.id != ADMIN_ID:
        return await message.answer("❌ Нет доступа")

    os.environ["NSFW_ENABLED"] = "true"
    await message.answer("🔞 NSFW режим включён")

# -----------------------------------------------------
# Команда выключения NSFW
# -----------------------------------------------------
async def disable_nsfw(message: Message):
    if message.from_user.id != ADMIN_ID:
        return await message.answer("❌ Нет доступа")

    os.environ["NSFW_ENABLED"] = "false"
    await message.answer("🟦 NSFW режим выключён")

# -----------------------------------------------------
# Проверка статуса
# -----------------------------------------------------
async def nsfw_status(message: Message):
    state = "ВКЛЮЧЕН" if NSFW_ENABLED else "ВЫКЛЮЧЕН"
    await message.answer(f"🔍 NSFW сейчас: {state}")

# -----------------------------------------------------
# Регистрация
# -----------------------------------------------------
def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(enable_nsfw, commands=["nsfw_on"])
    dp.register_message_handler(disable_nsfw, commands=["nsfw_off"])
    dp.register_message_handler(nsfw_status, commands=["nsfw"])