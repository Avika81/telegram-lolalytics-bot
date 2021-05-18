import logging
import time
#from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, Updater
from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    Filters,
    CallbackContext,
)

BASE_URL = 'https://lolalytics.com/lol/{CHAMPION_NAME}/build/'

def hello(update: Update, context: CallbackContext) -> None:
    logging.error(f'user_id: {update.effective_message.chat_id}')
    logging.error(update.message.text)
    champ_name = update.message.text.split(' ')[1]
    update.message.reply_text(f'Hello {update.effective_user.first_name}')
    update.message.reply_text('I think you want:')
    update.message.reply_text(BASE_URL.format(CHAMPION_NAME=champ_name.lower()))
    
    

BOT_NAME = 'lol_is_easy'
USERNAME = 'lol_is_easy_bot'
TOKEN = '1821126156:AAH3vSNq_D8n0IxtMwjLxzcbjv31O1NLC88' 

CHAT_ID = 516944707
def main() -> None:
    updater = Updater(TOKEN)
    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.start_polling()
        
    print('hello')

    # starts polling requests from telegram.

    
    time.sleep(5)
    print('exiting handler :)')
    
"""
USEFULL FUNCTIONS:
updater.bot.send_message(CHAT_ID, 'aaaa')
"""
if __name__ == '__main__':
    main()