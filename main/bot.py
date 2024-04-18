import logging
import os
import re
import sys

import requests
import telebot
from pygoogletranslation import Translator
from telebot import types
from transliterate import translit

# Get the bot token and weather API key from environment variables
BOT_TOKEN = "6425359689:AAFlmH2c6nma0zvVbr4ABCPgRVoQcGS40hk"
WEATHER_API_KEY = "3171b2c37c2a09802dd0b45d114c4d2a"

# Create a telebot instance
bot = telebot.TeleBot(BOT_TOKEN)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Regex pattern to detect Russian words
russian_pattern = re.compile(r"[А-Яа-яЁё]+")

# Dictionary to store user interactions
user_interaction_counter = {}

# List of Armenian cities
armenian_cities = [
    "Yerevan",
    "Gyumri",
    "Vanadzor",
    "Stepanakert",
    "Shushi",
    "Martuni",
    "Askeran",
    "Ivanyan",
    "Hrazdan",
    "Etchmiadzin",
    "Kapan",
    "Armavir",
    "Ararat",
    "Goris",
    "Ijevan",
    "Dilijan",
    "Martuni",
    "Masis",
    "Abovyan",
    "Artashat",
    "Charentsavan",
    "Sevan",
    "Gavar",
    # Add more cities as needed
]
channel_username = "@ArmenoScript"


# Function to create a menu using ReplyKeyboardMarkup
def create_inline_menu():
    # Create an inline keyboard markup
    markup = types.InlineKeyboardMarkup()

    # Add buttons to the markup
    button1 = types.InlineKeyboardButton(text="Armenian Latin => Armenian", callback_data="armenian_latin")
    button2 = types.InlineKeyboardButton(text="Russian => Armenian", callback_data="russian_armenian")
    button3 = types.InlineKeyboardButton(text="/weather", callback_data="weather")

    # Add buttons to the markup
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)

    return markup


# Function to create a menu for Armenian cities
def create_cities_menu():
    markup = types.InlineKeyboardMarkup()
    # Add Armenian cities to the menu as inline buttons
    for city in armenian_cities:
        button = types.InlineKeyboardButton(text=city, callback_data=city)
        markup.add(button)
    return markup


# Command handler for /start
@bot.channel_post_handler(commands=["start"])
def start_bot(message):
    menu = create_inline_menu()
    # Send a welcome message with the menu options
    # Build the API URL
    bot.send_message(message.chat.id, "Please choose an option:", reply_markup=menu)



# Command handler for /stop
@bot.channel_post_handler(commands=["stop"])
def stop_bot(message):
    bot.reply_to(message, "Bot is stopping. Կեցցե Հայաստան!")
    bot.reply_to(message, "Support me:")
    bot.reply_to(message, "https://buymeacoffee.com/haykeminyan")
    # Stop polling for messages
    bot.stop_polling()
    # Exit the program
    sys.exit(0)


# Command handler for /weather
@bot.channel_post_handler(commands=["weather"])
def show_weather_options(message):
    # Create the menu for cities
    cities_menu = create_cities_menu()
    bot.send_message(message.chat.id, "Please choose a city:", reply_markup=cities_menu)


# Handle callback queries from inline buttons
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    try:
        if call.data == "armenian_latin":
            bot.answer_callback_query(call.id, text="Please send the message you want to transliterate from Armenian Latin to Armenian.")
            @bot.channel_post_handler(func=lambda message: True)
            def handle_message(message):
                # Transliterate the message text to Armenian
                transliterated_text = translit(message.text, "hy")
                bot.reply_to(message, text=transliterated_text)

            # Add logic for Armenian Latin => Armenian conversion
        elif call.data == "russian_armenian":
            bot.answer_callback_query(call.id, text="Please send the message you want to translate from Russian to Armenian.")
            @bot.channel_post_handler(func=lambda message: True)
            def handle_message(message):
                # Translate the message text from Russian to Armenian
                translator = Translator()
                transliterated_text = translator.translate(message.text, dest="hy").text
                bot.reply_to(message, text=transliterated_text)
            # Add logic for Russian => Armenian translation
        elif call.data == "weather":
            # Provide the list of cities for weather info
            cities_menu = create_cities_menu()
            bot.answer_callback_query(call.id, text="Please choose a city:")

            @bot.channel_post_handler(func=lambda message: True)
            def handle_message(message):
                logger.info(message.text)
                # Fetch and respond with the current weather data for the chosen city
                city = message.text
                weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
                response = requests.get(weather_url)

                if response.status_code == 200:
                    data = response.json()
                    weather_description = data["weather"][0]["description"]
                    temperature = data["main"]["temp"]
                    weather_response = (
                        f"The current weather in {city}:\n"
                        f"Weather: {weather_description.capitalize()}\n"
                        f"Temperature: {temperature}°C"
                    )
                    bot.reply_to(message, text=weather_response)
                else:
                    bot.reply_to(message, text=f'Can not find {message.text}')

    except Exception as e:
        logger.error(f"Error occurred: {e}")
        bot.reply_to(message, "An unexpected error occurred. Please try again later.")




# Start polling for messages
bot.infinity_polling()
