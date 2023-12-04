"""Database for this application"""
from flask_pymongo import pymongo
from pymongo import MongoClient

CONNECTION_STRING = "mongodb://localhost:27017/"

client = MongoClient(CONNECTION_STRING)
db = client["database1"]
