"""Database for this application"""
from flask_pymongo import pymongo


CONNECTION_STRING = (
    r"mongodb+srv://exz209:06bW5AA1Z2X9YeON@cluster0.apy9mup.mongodb.net/?"
    "retryWrites=true&w=majority"
)


client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database("animals_db")
user_collection = pymongo.collection.Collection(db, "user_collection")
