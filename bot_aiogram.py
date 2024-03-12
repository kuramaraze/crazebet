from aiogram import Bot, Dispatcher, types
import asyncio
import config

token = config.TOKEN

async def start():
    bot = Bot(token)
    dp = Dispatcher(bot)

    try:
        await dp.start_polling()
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())