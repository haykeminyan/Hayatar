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
BOT_TOKEN = os.environ.get("BOT_TOKEN")
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")  # Weather API key

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
def create_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    # Add options to the menu
    markup.row(types.KeyboardButton("Armenian Latin => Armenian"))
    markup.row(types.KeyboardButton("Russian => Armenian"))
    markup.row(types.KeyboardButton("/weather"))
    return markup


# Function to create a menu for Armenian cities
def create_cities_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    # Add Armenian cities to the menu
    for city in armenian_cities:
        markup.row(types.KeyboardButton(city))
    return markup


# Command handler for /start
@bot.message_handler(commands=["start"])
def start_bot(message):
    menu = create_menu()
    # Send a welcome message with the menu options
    # Build the API URL
    bot.send_message(message.chat.id, "Please choose an option:", reply_markup=menu)


# Command handler for /stop
@bot.message_handler(commands=["stop"])
def stop_bot(message):
    api_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={channel_username}&text=Bot is stopping. Կեցցե Հայաստան!"
    # Send the request
    response = requests.get(api_url)
    bot.reply_to(message, "Bot is stopping. Կեցցե Հայաստան!")
    bot.reply_to(message, "Support me:")
    bot.reply_to(message, "https://buymeacoffee.com/haykeminyan")
    # Stop polling for messages
    bot.stop_polling()
    # Exit the program
    sys.exit(0)


# Command handler for /users
@bot.message_handler(commands=["users"])
def show_unique_number_users(message):
    unique_users = len(set(user_interaction_counter.keys()))
    description = f"This bot has {unique_users} unique users."
    api_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={channel_username}&text={description}"
    # Send the request
    response = requests.get(api_url)
    bot.reply_to(message, description)
    # Optional: you could also update the bot's description here


# Command handler for /weather
@bot.message_handler(commands=["weather"])
def show_weather_options(message):
    # Create the menu for cities
    cities_menu = create_cities_menu()
    bot.send_message(message.chat.id, "Please choose a city:", reply_markup=cities_menu)


# Message handler for any incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Increment the user interaction counter
        user_id = message.from_user.id
        if user_id not in user_interaction_counter:
            user_interaction_counter[user_id] = 0
        user_interaction_counter[user_id] += 1

        # Check if the message is one of the city names
        if message.text in armenian_cities:
            # Fetch and respond with the current weather data for the chosen city
            city = message.text
            weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
            response = requests.get(weather_url)
            data = response.json()

            if data.get("weather"):
                weather_description = data["weather"][0]["description"]
                temperature = data["main"]["temp"]
                weather_response = (
                    f"The current weather in {city}:\n"
                    f"Weather: {weather_description.capitalize()}\n"
                    f"Temperature: {temperature}°C"
                )
                # Build the API URL
                api_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={channel_username}&text={weather_response}"
                # Send the request
                response = requests.get(api_url)
                bot.reply_to(message, weather_response)
            else:
                api_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={channel_username}&text=Sorry, I couldn't fetch the weather data for {city}. Please try again later."
                # Send the request
                response = requests.get(api_url)
                # Handle API error
                bot.reply_to(
                    message,
                    f"Sorry, I couldn't fetch the weather data for {city}. Please try again later.",
                )

        elif message.text == "Armenian Latin => Armenian":
            api_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={channel_username}&text=Please send the message you want to transliterate from Armenian Latin to Armenian."
            # Send the request
            response = requests.get(api_url)
            # Ask the user to send a message for transliteration
            bot.reply_to(
                message,
                "Please send the message you want to transliterate from Armenian Latin to Armenian.",
            )
            return

        elif message.text == "Russian => Armenian":
            api_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={channel_username}&text=Please send the message you want to translate from Russian to Armenian."
            # Send the request
            response = requests.get(api_url)
            # Ask the user to send a message for translation
            bot.reply_to(
                message,
                "Please send the message you want to translate from Russian to Armenian.",
            )
            return

        # If the user chooses one of the options and then sends a message, handle the transliteration/translation
        if user_interaction_counter[user_id] > 1:
            if russian_pattern.search(message.text):
                # Translate the message text from Russian to Armenian
                translator = Translator()
                transliterated_text = translator.translate(message.text, dest="hy").text
                api_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={channel_username}&text={transliterated_text}"
                # Send the request
                response = requests.get(api_url)
                bot.reply_to(message, transliterated_text)
            else:
                # Transliterate the message text to Armenian
                transliterated_text = translit(message.text, "hy")
                api_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={channel_username}&text={transliterated_text}"
                # Send the request
                response = requests.get(api_url)
                bot.reply_to(message, transliterated_text)

    except Exception as e:
        logger.error(f"Error occurred: {e}")
        api_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={channel_username}&text=An unexpected error occurred. Please try again later."
        # Send the request
        response = requests.get(api_url)
        bot.reply_to(message, "An unexpected error occurred. Please try again later.")


# Start polling for messages
bot.infinity_polling()
