from aiogram import Dispatcher
from aiogram.types import Message
from services.model import generate_image
from services.billing import charge_user
from config import GENERATION_PRICE

# -----------------------------------------------------
# Обработка текста — запрос на генерацию
# -----------------------------------------------------
async def handle_generation(message: Message):
    prompt = message.text.strip()

    # Проверка баланса
    if not charge_user(message.from_user.id, GENERATION_PRICE):
        await message.answer("❌ Недостаточно кредитов. Пополните баланс или посмотрите рекламу.")
        return
    
    await message.answer("⏳ Генерация изображения... Это может занять до 15 секунд.")

    # Генерация изображения через модель
    result = generate_image(prompt)

    if result is None:
        await message.answer("❌ Ошибка генерации. Попробуйте другой запрос.")
    else:
        await message.answer_photo(result, caption="Готово! 🎨")

# -----------------------------------------------------
# Регистрация
# -----------------------------------------------------
def register_generate_handlers(dp: Dispatcher):
    dp.register_message_handler(handle_generation, regexp="^🎨 Генерация$")
    dp.register_message_handler(handle_generation)