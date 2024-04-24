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
db = client['telegram_bot']

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


# Function to retrieve user from the database
def get_user(user_id):
    return users_collection.find_one({'user_id': user_id})

