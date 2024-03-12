import telebot
from crypto_pay_api_sdk import Crypto

bot = telebot.TeleBot(token='7100874094:AAFPatgwwAx-P5u94o3QTnJrG7ReWvflBXA')
pay = Crypto(token='150544:AA1sPJvz5NkvN0tVy98ZjTG70YVxKTeKOZB')

@bot.message_handler(commands=['start'])
def get_id(message):
    id = message.chat.id
    inv = pay.createInvoice(asset='USDT', amount='0.5')
    bot.send_message(id, str(inv['result']['pay_url']))


bot.polling(none_stop=True)