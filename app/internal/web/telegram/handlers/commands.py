from telegram import Update
from telegram.ext import Updater, CallbackContext

def start(update: Update, context: CallbackContext) ->None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        f'Hi {user.mention_markdown_v2()}!',
    )

def help_command(update: Update, context: CallbackContext) ->None:
    update.message.reply_text('I can`t help you.'),

def about(update: Update, context: CallbackContext) ->None:
    update.message.reply_text('This bot is made for doing things. '),