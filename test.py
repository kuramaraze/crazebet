from aiogram import Bot, Dispatcher, types
from aiocryptopay import AioCryptoPay, Networks

bot = Bot(token='7059554676:AAGwcw-WuJfYUg6gtSVPfYSDBVi3JPQzRJs')
dp = Dispatcher(bot)

@dp.message