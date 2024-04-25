import logging
import os
import re
import sys

import requests
import telebot
from cencor import censor_profanity
from pygoogletranslation import Translator
from telebot import types
from transliterate import translit
from database import handle_user_registration, get_user, decrease_user_karma, show_users, increase_user_karma, get_user_username

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
    "Charbagh",
    "Vedi",
    "Ashtarak",
    "Shushi",
    "Karvachar",
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
    "Vardenis",
    "baku",
    "istanbul"
    # Add more cities as needed
]

# Global variable to track current mode
current_mode = None
# Fetch the bot's username
bot_info = bot.get_me()
bot_username = bot_info.username  # Store the bot's username


available_commands = [
    "/start - Start the bot and display the main menu",
    "/arm - Transliterate Armenian Latin to Armenian",
    "/rus - Translate Russian to Armenian",
    "/weather - Get weather information for a city",
    "/info - Get information about me :=)"
    # Add more commands here
]

# Function to handle mentions of the bot
@bot.channel_post_handler(
    func=lambda message: message.entities
    and any(
        entity.type == "mention"
        and message.text[entity.offset : entity.offset + entity.length]
        == f"@{bot_username}"
        for entity in message.entities
    )
)
def handle_mention(message):
    # Respond with a list of available commands
    bot.send_message(
        message.chat.id, "Available commands:\n" + "\n".join(available_commands)
    )


# Function to create a menu using ReplyKeyboardMarkup
def create_inline_menu():
    # Create an inline keyboard markup
    markup = types.InlineKeyboardMarkup()

    # Add buttons to the markup
    button1 = types.InlineKeyboardButton(
        text="Armenian Latin => Armenian", callback_data="armenian_latin"
    )
    button2 = types.InlineKeyboardButton(
        text="Russian => Armenian", callback_data="russian_armenian"
    )
    button3 = types.InlineKeyboardButton(text="Check Weather", callback_data="weather")

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
@bot.message_handler(
    func=lambda message: message.text
    and (
        message.text.startswith("/start@HayatarBot")
        or message.text.startswith("/start")
    )
)
def start_bot(message):
    menu = create_inline_menu()
    # Send a welcome message with the menu options
    # Build the API URL
    handle_user_registration(user_id=message.from_user.id, username=message.from_user.username,
                             chat_id=message.chat.id, karma=0)
    bot.send_message(message.chat.id, "Please choose an option:", reply_markup=menu)


@bot.message_handler(
    func=lambda message: message.text
    and (
        message.text.startswith("/info@HayatarBot") or message.text.startswith("/info")
    )
)
def info_bot(message):
    # Send a welcome message with the menu options
    # Build the API URL
    bot.send_message(
        message.chat.id,
        "Check out this professional profile on LinkedIn: https://www.linkedin.com/in/haykeminyan/",
    )
    bot.send_message(message.chat.id, "Support me:")
    bot.send_message(message.chat.id, "https://buymeacoffee.com/haykeminyan")


# Command handler for /stop
@bot.message_handler(
    func=lambda message: message.text
    and (
        message.text.startswith("/stop@HayatarBot") or message.text.startswith("/stop")
    )
)
def stop_bot(message):
    bot.reply_to(message, "Bot is stopping. Կեցցե Հայաստան!")
    # Stop polling for messages
    bot.stop_polling()
    # Exit the program
    sys.exit(0)


# Command handler for /weather
@bot.message_handler(
    func=lambda message: message.text
    and (
        message.text.startswith("/weather@HayatarBot")
        or message.text.startswith("/weather")
    )
)
def show_weather_options(message):
    # Create the menu for cities
    cities_menu = create_cities_menu()
    bot.send_message(message.chat.id, "Please choose a city:", reply_markup=cities_menu)


# Handle callback queries from inline buttons
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    global current_mode
    try:
        if call.data == "armenian_latin":
            current_mode = "armenian_latin"
            bot.answer_callback_query(
                call.id,
                text="Please send the message you want to transliterate from Armenian Latin to Armenian.",
            )

            # Add logic for Armenian Latin => Armenian conversion
        elif call.data == "russian_armenian":
            current_mode = "russian_armenian"
            bot.answer_callback_query(
                call.id,
                text="Please send the message you want to translate from Russian to Armenian.",
            )
            # Add logic for Russian => Armenian translation

        elif call.data == "weather":
            current_mode = "weather"
            bot.answer_callback_query(call.id, text="Please choose a city:")
            cities_menu = create_cities_menu()
            bot.send_message(
                call.message.chat.id, "Please choose a city:", reply_markup=cities_menu
            )
        else:
            # The user has selected a city
            current_mode = "weather"
            selected_city = call.data
            handle_weather(selected_city, call.message.chat.id)

    except Exception as e:
        logger.error(f"Error occurred: {e}")
        bot.send_message(
            call.message.chat.id,
            "An unexpected error occurred. Please execute /stop and /start.",
        )


# Handle /arm command
@bot.message_handler(
    func=lambda message: message.text
    and (message.text.startswith("/arm@HayatarBot") or message.text.startswith("/arm"))
)
def handle_arm_command(message):
    global current_mode
    # Set the current mode to Armenian Latin to Armenian
    current_mode = "arm"
    # Prompt the user to send a message for transliteration
    bot.send_message(
        message.chat.id,
        "Please send the message you want to transliterate from Armenian Latin to Armenian.",
    )


# Function to handle Armenian Latin => Armenian transliteration
@bot.message_handler(func=lambda message: current_mode == "arm")
def handle_armenian_latin_to_armenian(message):
    try:
        filtering_messages(message)
        transliterated_text = translit(message.text, "hy")
        # Reply with the transliterated text
        bot.reply_to(message, text=transliterated_text)
    except Exception as e:
        # Handle errors and send an error message
        logger.error(f"Error occurred: {e}")
        bot.reply_to(message, "An unexpected error occurred. Please try again later.")


@bot.message_handler(
    func=lambda message: message.text
    and (message.text.startswith("/rus@HayatarBot") or message.text.startswith("/rus"))
)
def handle_rus_command(message):
    global current_mode
    # Set the current mode to Armenian Latin to Armenian
    current_mode = "rus"
    # Prompt the user to send a message for transliteration
    bot.send_message(
        message.chat.id,
        "Please send the message you want to transliterate from Russian to Armenian.",
    )


@bot.message_handler(
    func=lambda message: message.text
    and (message.text.startswith("/users@HayatarBot") or message.text.startswith("/users"))
)
def handle_users_table(message):
    bot.send_message(chat_id=message.chat.id, text=show_users())


@bot.message_handler(
    func=lambda message: message.text
    and (message.text.startswith("/karma_plus@HayatarBot") or message.text.startswith("/karma_plus"))
)
def karma_plus(message):
    username = message.from_user.username
    parts = message.text.split()

    if len(parts) == 2:
        target_username = parts[1]
        logger.info(target_username)
        user_id = get_user_username(target_username.replace('@', ''))['user_id']
        if message.from_user.is_bot:
            increase_user_karma(user_id)
            bot.send_message(chat_id=message.chat.id,
                             text=f"Congratulations! {target_username} karma is increased! You karma now is {get_user(user_id)['karma']}")
        else:
            bot.send_message(chat_id=message.chat.id,
                             text=f'@{username} you are not allowed to change users karma! Vochxar!')
    else:
        bot.send_message(chat_id=message.chat.id,
                         text=f"Please write command correct /karma_plus@HaytarBot @username")


@bot.message_handler(
    func=lambda message: message.text
    and (message.text.startswith("/karma_minus@HayatarBot") or message.text.startswith("/karma_minus"))
)
def karma_minus(message):
    username = message.from_user.username
    parts = message.text.split()

    if len(parts) == 2:
        target_username = parts[1]
        user_id = get_user_username(target_username.replace('@', ''))['user_id']
        if message.from_user.is_bot:
            decrease_user_karma(user_id)
            bot.send_message(chat_id=message.chat.id,
                             text=f"Oops! {target_username} karma is decreased! You karma now is {get_user(user_id)['karma']}")
        else:
            bot.send_message(chat_id=message.chat.id,
                             text=f'@{username} you are not allowed to change users karma! Vochxar!')
    else:
        bot.send_message(chat_id=message.chat.id,
                         text=f"Please write command correct /karma_plus@HaytarBot @username")


# Function to handle Armenian Latin => Armenian transliterationd
@bot.message_handler(func=lambda message: current_mode == "rus")
def handle_russian_to_armenian(message):
    filtering_messages(message)
    try:
        translator = Translator()
        translated_text = translator.translate(message.text, dest="hy").text
        bot.reply_to(message, text=translated_text)
    except Exception as e:
        # Handle errors and send an error message
        logger.error(f"Error occurred: {e}")
        bot.reply_to(message, "An unexpected error occurred. Please try again later.")


def filtering_messages(message):
    username = message.from_user.username
    if "*" in censor_profanity(message.text):
        username_id = message.from_user.id
        decrease_user_karma(username_id)
        current_user = get_user(username_id)
        command = (
            f'@{username} -- "this message contains bad words and was deleted by bot"'
        )
        command2 = (f"@{username} reputation was downgraded. @{username} reputation is {current_user['karma']}")
        bot.send_message(chat_id=message.chat.id, text=command)
        bot.send_message(chat_id=message.chat.id, text=command2)
        bot.delete_message(chat_id=message.chat.id, message_id=message.id)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    logger.info('filtering'*10)
    filtering_messages(message)

    global current_mode
    try:
        if current_mode == "armenian_latin":
            transliterated_text = translit(message.text, "hy")
            bot.reply_to(message, text=transliterated_text)
        elif current_mode == "russian_armenian":
            translator = Translator()
            translated_text = translator.translate(message.text, dest="hy").text
            bot.reply_to(message, text=translated_text)
    except Exception as e:
        logger.error(e)


@bot.message_handler(func=lambda message: True)
def handle_weather(city, chat_id):
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(weather_url)
    if response.status_code == 200 and city.lower() not in ["baku", "istanbul"]:
        data = response.json()
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        weather_response = (
            f"The current weather in {city}:\n"
            f"Weather: {weather_description.capitalize()}\n"
            f"Temperature: {temperature}°C"
        )
        bot.send_message(chat_id, text=weather_response)
    elif city.lower() == "baku":
        bot.send_message(chat_id, text=f"Bakunakert is loading ...")
        bot.send_message(chat_id, text=f"Glory to Armenia!")
    elif city.lower() == "istanbul":
        bot.send_message(chat_id, text=f"Constantinople is loading ...")
        bot.send_message(chat_id, text=f"Glory to Armenia!")
    else:
        bot.send_message(chat_id, text=f"Cannot find weather information for {city}.")


# Start polling for messages
bot.infinity_polling()
