from telegram.ext import Updater
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import sys

token=sys.argv[1]
chatid=sys.argv[2]
message=sys.argv[3:-2]
button_name=sys.argv[-2]
button_url=sys.argv[-1]

updater = Updater(token=token)
dispatcher = updater.dispatcher

dispatcher.bot.send_message(chat_id=chatid, text=message, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(button_name, url=button_url)]]))