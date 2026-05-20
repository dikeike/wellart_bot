from aiogram import Dispatcher
from aiogram.types import Message
from services.ads import watch_ad

# -----------------------------------------------------
# Кнопка: посмотреть рекламу
# -----------------------------------------------------
async def handle_watch_ad(message: Message):
    reward = watch_ad(message.from_user.id)
    await message.answer(
        f"🎉 Спасибо за просмотр рекламы!\n"
        f"💰 Начислено: {reward} кредита(ов)."
    )

# -----------------------------------------------------
# Регистрация
# -----------------------------------------------------
def register_ads_handlers(dp: Dispatcher):
    dp.register_message_handler(handle_watch_ad, regexp="^📺 Реклама$")