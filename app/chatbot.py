from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.filters import CommandStart

bot = Bot(token="7844711595:AAGcBYdR05B2dnysqIxyW6BVN9_opQrXMeA")
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(
        "Привет! Я бот, который поможет тебе в выборе качественного отдыха! Я - являюсь ботом который подбирает на основе современных алгоритмов. Например, ты приехал в город Калининград в первый раз! Я помогу тебе подобрать места именно по твоим интересам!")


@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)
    await message.reply(message.text)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
