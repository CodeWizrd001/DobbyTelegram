import telegram
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def bop(bot, update):
    print("Bop Invoked")
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    '''print(chat_id)
    print(update)
    print(help(bot))'''

def Help(bot, update) :
    chat_id = update.message.chat_id
    bot.send_text("Help")
    print("Invoked Bot Help")
    '''print(chat_id)
    print(update)
    print(bot)'''


global updater
global dp
global dp1
updater = Updater('994787768:AAEQRpT5yjdeSxvFVvgnsFGirA4og0MWTI8')
dp = updater.dispatcher
dp.add_handler(CommandHandler('bop',bop))
dp.add_handler(CommandHandler('help',Help))
updater.start_polling()
updater.idle()

if __name__ == '__main__':
    pass
