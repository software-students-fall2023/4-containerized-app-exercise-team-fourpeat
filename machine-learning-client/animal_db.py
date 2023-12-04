"""Database for this application"""
from pymongo import MongoClient
import os

DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
CONNECTION_STRING = f"mongodb://{DATABASE_HOST}:27017/"

client = MongoClient(CONNECTION_STRING)
db = client["database1"]
