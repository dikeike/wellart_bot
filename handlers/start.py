from aiogram import Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

# -----------------------------------------------------
# Главное меню
# -----------------------------------------------------
def get_main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(
        KeyboardButton("🎨 Генерация"),
        KeyboardButton("🖼 Модификация")
    )
    kb.add(
        KeyboardButton("💰 Баланс"),
        KeyboardButton("📺 Реклама")   # ← новая кнопка
    )
    kb.add(
        KeyboardButton("⚙️ Настройки")
    )
    return kb


# -----------------------------------------------------
# Команда /start
# -----------------------------------------------------
async def cmd_start(message: Message):
    await message.answer(
        "👋 Добро пожаловать в Wellart!\n"
        "Создавай и модифицируй изображения с помощью AI.",
        reply_markup=get_main_menu()
    )


# -----------------------------------------------------
# Регистрация
# -----------------------------------------------------
def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])