#!/usr/bin/python
from telegram.ext import Updater
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import os

token=os.getenv('INPUT_TOKEN')
chatid=os.getenv('INPUT_CHATID')
message=os.getenv('INPUT_MESSAGE')
button=os.getenv('INPUT_BUTTON')
button_name=os.getenv('INPUT_BUTTON_NAME')
button_url=os.getenv('INPUT_BUTTON_URL')

updater = Updater(token=token)
dispatcher = updater.dispatcher

if(button):
    dispatcher.bot.send_message(chat_id=chatid, text=str(message), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(button_name, url=button_url)]]))
else:
    dispatcher.bot.send_message(chat_id=chatid, text=str(message))
    
