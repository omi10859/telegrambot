from telegram.ext import Updater, CommandHandler
from telegram.ext import ChatAction
from datetime import datetime, timedelta
from pytz import timezone
from time import sleep
import logging,requests,pytz,re,ast

def start(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    sleep(0.3)
    bot.sendMessage.chat_id, text='OMG!! Im working look I can say heyy'

def hello(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    sleep(0.3)
   bot.sendMessage.chat_id, text='H@ll~~!! I will kill you'
def help(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    sleep(0.3)
    bot.sendMessage.chat_id, text=''''Use one of the following commands
/mailinglist - to get my email id
/facebook - to get a link of my facebook page 
/github - to get a link to PyDelhi Github page
To contribute to|modify this bot : https://github.com/omi10859/telegrambot ''''


updater = Updater('YOUR TOKEN HERE')
dispatcher=updater.dispatcher
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
update.dispatcher.add_handler(CommandHandler('help', help))

updater.start_polling()
updater.idle()