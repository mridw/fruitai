from pymongo import MongoClient
from urllib.parse import quote_plus

def get_db():
    username = quote_plus('fruisai')
    password = quote_plus('fruitsai@1234')  # Properly escape special characters
    connection_string = f'mongodb+srv://{username}:{password}@fruitai.4cjbr.mongodb.net/?retryWrites=true&w=majority&appName=FruitAi'
    client = MongoClient(connection_string)
    db = client['fruitsai']  # Replace with your database name
    return db
