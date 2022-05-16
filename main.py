from telegram.ext import Updater
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import sys
import os

token=sys.argv[1]
chatid=sys.argv[2]
message=""
button_name=sys.argv[-2]
button_url=sys.argv[-1]

for i in sys.argv[3:-2]:
    message+=i+'\n\n'

os.getenv('INPUT_message')
os.environ.get('INPUT_message')
message = os.environ['INPUT_message']

updater = Updater(token=token)
dispatcher = updater.dispatcher

dispatcher.bot.send_message(chat_id=chatid, text=str(message), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(button_name, url=button_url)]]))