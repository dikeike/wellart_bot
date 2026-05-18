from aiogram import Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

# -----------------------------------------------------
# Кнопки главного меню
# -----------------------------------------------------
def main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(
        KeyboardButton("🎨 Генерация"),
        KeyboardButton("🖼 Модификация"),
    )
    kb.add(
        KeyboardButton("💰 Баланс"),
        KeyboardButton("⚙️ Настройки"),
    )
    return kb

# -----------------------------------------------------
# Команда /start
# -----------------------------------------------------
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я WellArt — искусственный интеллект для создания и модификации изображений.\n\n"
        "Выбирай действие на клавиатуре 👇",
        reply_markup=main_menu(),
    )

# -----------------------------------------------------
# Регистрация хендлеров
# -----------------------------------------------------
def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])