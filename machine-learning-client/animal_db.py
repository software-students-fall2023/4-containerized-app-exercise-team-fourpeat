"""Database for this application"""
import os
from pymongo import MongoClient

DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
CONNECTION_STRING = f"mongodb://{DATABASE_HOST}:27017/"

client = MongoClient(CONNECTION_STRING)
db = client["database1"]
