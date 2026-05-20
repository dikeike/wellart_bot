import requests
from io import BytesIO
from aiogram import Bot
from config import OPENAI_API_KEY, NSFW_ENABLED

# -----------------------------------------------------
# Заглушка для генерации изображений
# (в MVP мы возвращаем рандомную картинку с сайта)
# ПОТОМ сюда добавим реальную AI модель!
# -----------------------------------------------------

def generate_image(prompt: str):
    """
    Заглушка генерации.
    Вместо модели — берём случайное изображение с picsum.photos
    """
    try:
        url = "https://picsum.photos/1024.jpg"
        img_bytes = requests.get(url).content
        return BytesIO(img_bytes)
    except Exception:
        return None


# -----------------------------------------------------
# Заглушка модификации изображений
# -----------------------------------------------------
def modify_image(file_id: str):
    """
    Заглушка модификации.
    В реальности мы будем отправлять фото в модель.
    Пока — просто выдаём другое случайное изображение.
    """
    try:
        url = "https://picsum.photos/1025.jpg"
        img_bytes = requests.get(url).content
        return BytesIO(img_bytes)
    except Exception:
        return None