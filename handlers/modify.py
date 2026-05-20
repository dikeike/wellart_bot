from aiogram import Dispatcher
from aiogram.types import Message
from services.model import modify_image
from services.billing import charge_user
from config import MODIFY_PRICE

# -----------------------------------------------------
# Модификация изображения
# -----------------------------------------------------
async def handle_modify(message: Message):
    if not message.photo:
        await message.answer("Пожалуйста, отправьте фото, которое нужно изменить 🖼")
        return

    # Проверка баланса пользователя
    if not charge_user(message.from_user.id, MODIFY_PRICE):
        await message.answer("❌ Недостаточно кредитов. Пополните баланс или посмотрите рекламу.")
        return

    await message.answer("⏳ Модифицирую изображение...")

    file_id = message.photo[-1].file_id

    result = modify_image(file_id)

    if result is None:
        await message.answer("❌ Ошибка обработки изображения.")
    else:
        await message.answer_photo(result, caption="Готово! 🛠")

# -----------------------------------------------------
# Регистрация
# -----------------------------------------------------
def register_modify_handlers(dp: Dispatcher):
    dp.register_message_handler(handle_modify, regexp="^🖼 Модификация$")
    dp.register_message_handler(handle_modify, content_types=["photo"])