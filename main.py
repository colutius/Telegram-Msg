#!/usr/bin/python
from telegram.ext import Updater
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import os

token = os.getenv('INPUT_TOKEN')
chatid = os.getenv('INPUT_CHATID')
message = os.getenv('INPUT_MESSAGE')
button = os.getenv('INPUT_BUTTON')
button_name = os.getenv('INPUT_BUTTON_NAME')
button_url = os.getenv('INPUT_BUTTON_URL')
is_notify = os.getenv('INPUT_IS_NOTIFY')
is_preview = os.getenv('INPUT_IS_PREVIEW')

updater = Updater(token=token)
dispatcher = updater.dispatcher

# button
if (button == "true"):
    button = InlineKeyboardMarkup(
        [[InlineKeyboardButton(button_name, url=button_url)]])
else:
    button = None

# notify
if (is_notify == "true"):
    is_notify = True
else:
    is_notify = False

# preview
if (is_preview == "true"):
    is_preview = True
else:
    is_preview = False

dispatcher.bot.send_message(chat_id=chatid,
                            text=str(message),
                            reply_markup=button,
                            disable_notification=is_notify,
                            disable_web_page_preview=is_preview)
