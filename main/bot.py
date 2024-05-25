import datetime
import logging
import os
import re
import sys
from functools import reduce
from profanity_check import predict, predict_prob
from armenian_transliterate import armenian_latin_to_armenian_hy
import pytz
import requests
from datetime import timedelta
import telebot
from cencor import censor_profanity
from pygoogletranslation import Translator
from telebot import types
from database import get_user, decrease_user_karma, show_users, increase_user_karma, get_user_username, \
    check_if_user_registrated, get_user_first_name, update_user_karma_in_mongo

# Get the bot token and weather API key from environment variables
BOT_TOKEN = "6425359689:AAFlmH2c6nma0zvVbr4ABCPgRVoQcGS40hk"
WEATHER_API_KEY = "3171b2c37c2a09802dd0b45d114c4d2a"
last_message_time = {}
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
    "/start - Starts the bot and displays the main menu with available options",
    "/weather - Allows users to check the weather information for different cities",
    "/arm - Transliterates Armenian Latin text to Armenian script",
    "/rus - Translates Russian text to Armenian",
    "/rules_en - Rules in chat in English",
    "/rules_arm - Rules in chat in Armenian",
    "/rules_es - Rules in chat in Spanish",
    "/rules_ru - Rules in chat in Russian",
    "/users - Displays a table of registered users.",
    "/karma_plus - Increases the karma of a specified user (Admin-only)",
    "/karma_minus - Decreases the karma of a specified user (Admin-only)",
    "Mentions - When the bot is mentioned, it responds with a list of available commands",
    "mute - Mute users",
    "/info - Provides information about the developer and his bio",
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


def is_user_admin(chat_id, user_id):
    try:
        chat_administrators = bot.get_chat_administrators(chat_id)
        logger.info(chat_administrators)
        logger.info('!'*100)
        for admin in chat_administrators:
            logger.error(admin)
            logger.info('!'*1000)
            logger.info(admin.status)
            logger.info('!'*1000)
            if admin.status in ['creator', 'administrator']:
                return True
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def admin_only(func):
    def wrapper(message):
        if is_user_admin(message.chat.id, message.from_user.id):
            return func(message)
        else:
            bot.reply_to(message, "You are not authorized to use this command, Vochxar!")
    return wrapper


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
    bot.send_message(message.chat.id, "Please choose an option:", reply_markup=menu)


@bot.message_handler(
    func=lambda message: message.text
    and (
        message.text.startswith("/rules_en@HayatarBot")
        or message.text.startswith("/rules_en")
    )
)
def rules_en(message):
    # Read the content of the Markdown file
    with open('/app/main/rules/rules_en.md', 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    # Send the content of the file as a message
    bot.send_message(chat_id=message.chat.id,
                     text=markdown_content,
                     parse_mode="Markdown")

@bot.message_handler(
    func=lambda message: message.text
    and (
        message.text.startswith("/rules_arm@HayatarBot")
        or message.text.startswith("/rules_arm")
    )
)
def rules_arm(message):
    # Read the content of the Markdown file
    with open('/app/main/rules/rules_arm.md', 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    # Send the content of the file as a message
    bot.send_message(chat_id=message.chat.id,
                     text=markdown_content,
                     parse_mode="Markdown")

@bot.message_handler(
    func=lambda message: message.text
    and (
        message.text.startswith("/rules_es@HayatarBot")
        or message.text.startswith("/rules_es")
    )
)
def rules_es(message):
    # Read the content of the Markdown file
    with open('/app/main/rules/rules_es.md', 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    # Send the content of the file as a message
    bot.send_message(chat_id=message.chat.id,
                     text=markdown_content,
                     parse_mode="Markdown")


@bot.message_handler(
    func=lambda message: message.text
    and (
        message.text.startswith("/rules_ru@HayatarBot")
        or message.text.startswith("/rules_ru")
    )
)
def rules_ru(message):
    # Read the content of the Markdown file
    with open('/app/main/rules/rules_ru.md', 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    # Send the content of the file as a message
    bot.send_message(chat_id=message.chat.id,
                     text=markdown_content,
                     parse_mode="Markdown")


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
        transliterated_text = armenian_latin_to_armenian_hy(message.text)
        if predict_prob([message.text]) > 0.8:
            bot.reply_to(message, "Please be more polite! Calm down ara!")
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
@admin_only
def karma_plus(message):
    parts = message.text.split()

    if len(parts) == 2:
        target_username = parts[1]
        logger.info(target_username)
        try:
            user = get_user_username(target_username.replace('@', ''))['user_id']
        except (KeyError, TypeError):
            user = get_user_first_name(target_username.replace('@', ''))['user_id']

        increase_user_karma(user)
        bot.send_message(chat_id=message.chat.id,
                         text=f"Congratulations! {target_username} karma is increased! You karma now is {get_user(user)['karma']}")

    else:
        bot.send_message(chat_id=message.chat.id,
                         text=f"Please write command correct /karma_plus@HaytarBot @username")


@bot.message_handler(
    func=lambda message: message.text
    and (message.text.startswith("/karma_minus@HayatarBot") or message.text.startswith("/karma_minus"))
)
@admin_only
def karma_minus(message):
    username = message.from_user.username
    parts = message.text.split()

    if len(parts) == 2:
        target_username = parts[1]
        user_id = get_user_username(target_username.replace('@', ''))['user_id']
        decrease_user_karma(user_id)
        bot.send_message(chat_id=message.chat.id,
                         text=f"Oops! {target_username} karma is decreased! You karma now is {get_user(user_id)['karma']}")

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


def send_admin(message):
    # Assuming the admin's Telegram ID is known and stored in admin_id
    admin_id_hayk = '199327249'
    admin_id_mik = '6712061401'
    bot.send_message(admin_id_hayk, f"Message from @{message.from_user.first_name}: {message.text}")
    bot.send_message(admin_id_mik, f"Message from @{message.from_user.first_name}: {message.text}")
    bot.reply_to(message, text='Thanks! Message was sent to admin user!')


@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_members(message):
    for new_member in message.new_chat_members:
        if not new_member.is_bot:
            bot.send_message(message.chat.id, f"Welcome @{new_member.first_name} to our group! We're glad to have you here.")


@bot.message_handler(
    func=lambda message: message.text
    and (
        message.text.startswith("/message_admin@HayatarBot")
        or message.text.startswith("/message_admin")
    )
)
def message_admin(message):
    bot.reply_to(message, text=f"Please send message to admin")
    bot.register_next_step_handler(message, send_admin)


def kick_user_to_hell(message, karma, bot):
    user_id = message.from_user.id
    if karma < -2 and not is_user_admin(chat_id=message.chat.id, user_id=user_id):
        bot.kick_chat_member(
            chat_id=message.chat.id,
            user_id=message.from_user.id,
        )  #
        user = get_user(user_id=message.from_user.id)
        logger.info(user)
        logger.info('!'*100)
        update_user_karma_in_mongo(user_id=user['user_id'], new_karma=0)
        # Notify users that the user has been banned
        bot.send_message(chat_id=message.chat.id, text="User has been banned. Բարի գալուստ գյորբագոր.")


def filtering_messages(message):
    check_if_user_registrated(message, bot)
    user_id = message.from_user.id
    if not is_user_admin(chat_id=message.chat.id, user_id=user_id):
        flood_detection(message)

    logger.info(predict_prob([message.text]))

    if predict_prob([message.text]) > 0.8:
        bot.reply_to(message, "Please be more polite! Calm down ara!")
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
        kick_user_to_hell(message, current_user['karma'], bot)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    filtering_messages(message)

    global current_mode
    try:
        if current_mode == "armenian_latin":
            transliterated_text = armenian_latin_to_armenian_hy(message.text)
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


# logic {'user_id': [timestamp values of date]}
detector = {}


def flood_detection(message):
    # Get the current time
    current_time = pytz.timezone('Asia/Yerevan')
    current_time_yerevan = datetime.datetime.now(current_time)
    # Calculate the future time when the restriction will be lifted (e.g., 30 seconds from now)
    until_time = current_time_yerevan + timedelta(seconds=30)
    # Convert the future time to a Unix timestamp
    until_timestamp = int(until_time.timestamp())
    user_id = message.from_user.id
    timestamp = message.date

    if user_id in detector:
        # If the user_id already exists in the detector dictionary, append the timestamp to its list
        detector[user_id].append(timestamp)
    else:
        # If the user_id doesn't exist in the detector dictionary, create a new entry with the timestamp
        detector[user_id] = [timestamp]

    for potential_user_id, timestamps in detector.items():
        for i in range(len(timestamps) - 1):

            logger.info(timestamps)
            total_subtraction = sorted([timestamps[i] - timestamps[i + 1] for i in range(len(timestamps) - 1)])[0]

            if abs(total_subtraction) <= 10 and len(timestamps) > 4:
                username = get_user(potential_user_id)['username']
                if username is None:
                    username = potential_user_id
                    detector.clear()
                    timestamps.clear()
                    bot.send_message(chat_id=message.chat.id,
                                     text=f"User with id {username} have been muted for a 30 seconds. Գնացեք և հանգստացեք!")

                    bot.restrict_chat_member(message.chat.id, potential_user_id, until_date=until_timestamp)
                else:
                    logger.error(get_user(potential_user_id))
                    detector.clear()
                    timestamps.clear()
                    bot.send_message(chat_id=message.chat.id,
                                     text=f"You @{username} have been muted for a 30 seconds. Գնացեք և հանգստացեք!")
                    bot.restrict_chat_member(message.chat.id, potential_user_id, until_date=until_timestamp)


@bot.message_handler(
    func=lambda message: message.text
    and (message.text.startswith("/mute@HayatarBot") or message.text.startswith("/mute"))
)
@admin_only
def muting_user(message):
    username = message.from_user.username
    parts = message.text.split()
    # Get the current time
    current_time = pytz.timezone('Asia/Yerevan')
    current_time_yerevan = datetime.datetime.now(current_time)
    # Calculate the future time when the restriction will be lifted (e.g., 30 seconds from now)
    until_time = current_time_yerevan + timedelta(seconds=30)
    # Convert the future time to a Unix timestamp
    until_timestamp = int(until_time.timestamp())
    logger.info(parts)
    logger.info('!'*10000)
    logger.info(dir(message.from_user))
    if len(parts) == 2:
        target_username = parts[1]
        user_id = get_user_username(target_username.replace('@', ''))['user_id']
        if is_user_admin(chat_id=message.chat.id, user_id=user_id):
            bot.send_message(chat_id=message.chat.id,
                             text=f"Oops! {target_username} is muted for 30 seconds!")
            bot.restrict_chat_member(message.chat.id, user_id, until_date=until_timestamp)
        else:
            bot.send_message(chat_id=message.chat.id,
                             text=f'@{username} you are not allowed to mute users! Vochxar!')
    else:
        bot.send_message(chat_id=message.chat.id,
                         text=f"Please write command correct /mute@HaytarBot @username")


@bot.message_handler(
    func=lambda message: message.text
    and (message.text.startswith("/ban@HayatarBot") or message.text.startswith("/ban"))
)
@admin_only
def ban_user(message):
    username = message.from_user.username
    parts = message.text.split()
    if len(parts) == 2:
        target_username = parts[1]
        user_id = get_user_username(target_username.replace('@', ''))['user_id']
        logger.info(user_id)
        logger.info('?'*100)
        bot.ban_chat_member(
            chat_id=message.chat.id,
            user_id=user_id,
        )  #


# Start polling for messages
bot.infinity_polling()
