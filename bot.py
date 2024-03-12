import config  # token
import telebot
import telebot.types
from crypto_pay_api_sdk import Crypto

bot = telebot.TeleBot(token=config.TOKEN)
pay = Crypto(token=config.PAYTOKEN)
pay.createInvoice(asset='USDT', amount=)

@bot.message_handler(commands=['start'])