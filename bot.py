import os
import time

import requests
import telebot
from transliterate import translit, get_available_language_codes

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)
bot.timeout = 100  # Increase timeout as needed (in seconds)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Extract the text from the message
        message_text = message.text

        # Transliterate the message text to Armenian (hy)
        transliterated_text = translit(message_text, 'hy')

        # Reply to the user with the transliterated text
        bot.reply_to(message, transliterated_text)

    except requests.exceptions.ReadTimeout:
        # Log the error and retry after a short wait
        print("ReadTimeout occurred, retrying...")
        time.sleep(5)  # Wait for 5 seconds before retrying
        handle_message(message)


bot.infinity_polling()
