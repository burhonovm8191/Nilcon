from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import json

TOKEN = "8758176743:AAFsLHHB1BLWTlqSr8j4yFOXr5BtvaT11Ns"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        "Хуш омадед ба портали деҳаи Нилкон 🌍\n"
        "Ба сайт: https://username.github.io/nilkon"
    )

@dp.message_handler(commands=["news"])
async def send_news(message: types.Message):
    with open('news.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for item in data:
        await message.answer(f"{item['title']}\n{item['content']}")

executor.start_polling(dp)