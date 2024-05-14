import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, filters
from telegram import Update
from telegram.ext import filters

logging.basicConfig(level=logging.INFO)

from config import BOT_TOKEN

def start(update: Update, context: CallbackContext):
    try:
        update.message.reply_text('Hello I\'m a bot.')
    except Exception as e:
        logging.error(f'Error in start command: {e}')

def echo(update: Update, context: CallbackContext):
    try:
        update.message.reply_text(update.message.text)
    except Exception as e:
        logging.error(f'Error in echo message: {e}')

def main():
    try:
        updater = Updater(BOT_TOKEN, use_context=True)

        dp = updater.dispatcher

        dp.add_handler(CommandHandler('start', start))
        dp.add_handler(MessageHandler(filters.text & ~filters.command, echo))  # Use Filters.text & ~Filters.command to filter out commands

        updater.start_polling()
        updater.idle()
    except Exception as e:
        logging.error(f'Error in main: {e}')

if __name__ == '__main__':
    main()
