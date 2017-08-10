from telegram.ext import Updater
updater = Updater(token='448097907:AAFt-I1seXFQccixXQqgDQq4Dch4i0gLg48')
dispatcher = updater.dispatcher
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="abe chodu..so ja bc")
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()




