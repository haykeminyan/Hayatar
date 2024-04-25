from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from datetime import datetime
import time


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
def handle_user_registration(user_id, username, chat_id, karma):
    user_data = {
        'user_id': user_id,
        'username': username,
        'chat_id': chat_id,
        'karma': karma,
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


def update_user_karma_in_mongo(user_id, new_karma):
    # Update the user's karma in the collection
    users_collection.update_one(
        {"user_id": user_id},
        {"$set": {"karma": new_karma}}
    )


# Function to retrieve user from the database
def get_user(user_id):
    return users_collection.find_one({'user_id': user_id})


def show_users():
    cursor = users_collection.find({}, {'_id': 0, 'username': 1, 'karma': 1, 'date_joined': 1})
    users_data = list(cursor)  # Convert cursor to a list of dictionaries

    # Check if there are users in the database
    if not users_data:
        return "No users found."

    table = """```
$Username$          | $Karma$            | $Date Joined$
--------------------|--------------------|--------------------
"""

    # Iterate over each user's data and add it to the table
    for user in users_data:
        # Format the user data and add it to the table
        table += f"{user['username']: <20} | {user['karma']: <17} | {user['date_joined']}\n"

    # Close the code block
    table += "```"
    return table


