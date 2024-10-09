# Run this command in the terminal to install flask framework:
# pip install flask

# To import the flask framework, we use:
from flask import Flask
from pymongo import MongoClient  # pip install pymongo
from dotenv import load_dotenv
import os

load_dotenv()

db_username = os.environ["MONGODB_USERNAME"]
db_password = os.environ["MONGODB_PASSWORD"]

print(db_username)
app = Flask(__name__)

# MongoDB Atlas Client
client = MongoClient(f"mongodb+srv://{db_username}:{db_password}@cluster0.ktsh8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

app_db = client.app  # app is the name of the database in MongoDB Atlas
products_collection = app_db.products  # products is the name of the collection inside the database

from app import routes