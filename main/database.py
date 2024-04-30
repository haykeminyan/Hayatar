from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from datetime import datetime
import time
import logging

logger = logging.getLogger(__name__)


def wait_for_mongo(db_url, max_attempts=10, sleep_time=2):
    client = MongoClient(db_url)
    attempts = 0
    while attempts < max_attempts:
        try:
            # The ismaster command is cheap and does not require auth.
            client.admin.command('ismaster')
            return client
        except ConnectionFailure:
            print(f"Waiting for MongoDB at {db_url}...")
            time.sleep(sleep_time)
            attempts += 1
    raise ConnectionFailure("MongoDB not available")


# Use the function in your main script
MONGODB_URL = "mongodb://mongodb:27017/node-boilerplate"
client = wait_for_mongo(MONGODB_URL)

# Choose or create a database
db = client['mongo']

# Choose or create a collection
users_collection = db['users']


# Function to add user to MongoDB
def add_user_to_mongo(user_data):
    existing_user = users_collection.find_one({'user_id': user_data['user_id']})
    if existing_user is None:
        users_collection.insert_one(user_data)


# Example function to handle user registration from a chat
def handle_user_registration(user_id, username, first_name, last_name, chat_id, karma, is_premium):
    user_data = {
        'user_id': user_id,
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
        'chat_id': chat_id,
        'karma': karma,
        'is_premium': is_premium,
        'date_joined': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    add_user_to_mongo(user_data)


def decrease_user_karma(user_id):
    # Retrieve user data from MongoDB based on user_id
    user = get_user(user_id)
    if user:
        current_karma = user['karma']
        # Decrease karma by 1 (or any other value as needed)
        new_karma = current_karma - 1  # Ensure karma doesn't go below 0
        # Update user data in MongoDB with the new karma value
        update_user_karma_in_mongo(user_id, new_karma)


def increase_user_karma(user_id):
    # Retrieve user data from MongoDB based on user_id
    user = get_user(user_id)
    if user:
        current_karma = user['karma']
        # Decrease karma by 1 (or any other value as needed)
        new_karma = current_karma + 1  # Ensure karma doesn't go below 0
        # Update user data in MongoDB with the new karma value
        update_user_karma_in_mongo(user_id, new_karma)


def update_user_karma_in_mongo(user_id, new_karma):
    # Update the user's karma in the collection
    users_collection.update_one(
        {"user_id": user_id},
        {"$set": {"karma": new_karma}}
    )


# Function to retrieve user from the database
def get_user(user_id):
    return users_collection.find_one({'user_id': user_id})


def get_user_username(username):
    return users_collection.find_one({'username': username})

def get_user_first_name(first_name):
    return users_collection.find_one({'first_name': first_name})


def show_users():
    cursor = users_collection.find({}, {'_id': 0, 'username': 1, 'karma': 1, 'date_joined': 1})
    users_data = list(cursor)  # Convert cursor to a list of dictionaries

    # Check if there are users in the databasef
    if not users_data:
        return "No users found."
    users_data_sorted = sorted(users_data, key=lambda x: x['karma'], reverse=True)
    emojies = [{'emojie': '🥇'}, {'emojie':'🥈'}, {'emojie':'🥉'}]

    users_data_sorted_emoj = list(zip(users_data_sorted, emojies[:len(users_data_sorted)]))
    # Append any remaining elements from the longer array to the zipped
    if len(emojies) < len(users_data_sorted_emoj):
        users_data_sorted_emoj += emojies[len(users_data_sorted):]
    table = """ 🏆 Leaderboard """ + '\n'

    # Iterate over each user's data and add it to the table
    for user in users_data_sorted_emoj:
        if len(user) == 2:
            user[0]['emojie'] = user[1]['emojie']
            del user[1]['emojie']
            user = [i for i in user if i]
        # Format the user data and add it to the table
        try:
            if user[0]['username'] is not None:
                table_str = user[0]['emojie'] + '\t'*2 +f"@{user[0]['username']}" + ' '*5 + f"{user[0]['karma']}  karma" + '\n'
            else:
                table_str = user[0][
                                'emojie'] + '\t' * 2 + f"@{user[0]['first_name']}" + ' ' * 5 + f"{user[0]['karma']}  karma" + '\n'
        except KeyError:
            if user[0]['username'] is not None:
                table_str = f"@{user[0]['username']}" + ' ' * 5 + f"{user[0]['karma']} karma"
            else:
                table_str = f"@{user[0]['first_name']}" + ' ' * 5 + f"{user[0]['karma']} karma"
        table += '\n' + str(table_str)

    table += """  """
    return table


def check_if_user_registrated(message, bot):
    if not get_user(message.from_user.id):
        bot.send_message(chat_id=message.chat.id, text=f"Welcome @{message.from_user.username} to @ArmenoScriptChat! Please check our rules /rules_en")
        with open('/app/main/rules/rules_en.md', 'r', encoding='utf-8') as file:
            markdown_content = file.read()

        # Send the content of the file as a message
        bot.send_message(chat_id=message.chat.id,
                         text=markdown_content,
                         parse_mode="Markdown")
        handle_user_registration(user_id=message.from_user.id, username=message.from_user.username,
                                 first_name=message.from_user.first_name,
                                 last_name=message.from_user.last_name,
                                 is_premium=message.from_user.is_premium,
                                 chat_id=message.chat.id, karma=0)


def kick_user_to_hell(message, karma, bot):
    if karma < -2 and not message.from_user.is_bot:
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


