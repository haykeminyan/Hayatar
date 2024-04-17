import os

import telebot
from transliterate import translit
import re

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)
bot.timeout = 100  # Increase timeout as needed (in seconds)
russian_pattern = re.compile(r'[А-Яа-яЁё]+')


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Extract the text from the message
        message_text = message.text

        # Check if the message contains Russian words
        if russian_pattern.search(message_text):
            # Translate the message text from Russian to Armenian
            translated_text = translit(message_text, 'ru', reversed=True)
            transliterated_text = translit(translated_text, 'hy')

            # Reply to the user with the translated text
            bot.reply_to(message, transliterated_text)
        else:
            # Transliterate the message text to Armenian
            transliterated_text = translit(message_text, 'hy')

            # Reply to the user with the transliterated text
            bot.reply_to(message, transliterated_text)
    except AttributeError as e:
        # Log the error and reply with an error message
        print("Error translating message:", e)
        bot.reply_to(message, "An error occurred during translation. Please try again later.")
    except Exception as e:
        # Handle other exceptions
        print("An unexpected error occurred:", e)
        bot.reply_to(message, "An unexpected error occurred. Please try again later.")


bot.infinity_polling()
