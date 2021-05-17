import logging
#from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, Updater
from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    Filters,
    CallbackContext,
)

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


BOT_NAME = 'lol_is_easy'
USERNAME = 'lol_is_easy_bot'
TOKEN = '1821126156:AAH3vSNq_D8n0IxtMwjLxzcbjv31O1NLC88' 

def main() -> None:
    updater = Updater(TOKEN)
    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    print('hello')
    
if __name__ == '__main__':
    main()