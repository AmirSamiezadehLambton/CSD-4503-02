# Run this command in the terminal to install flask framework:
# pip install flask

# To import the flask framework, we use:
from flask import Flask
from pymongo import MongoClient  # pip install pymongo

app = Flask(__name__)

# MongoDB Atlas Client
client = MongoClient("mongodb+srv://root:dBAxAFAZS3t43anh@cluster0.ktsh8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

app_db = client.app  # app is the name of the database in MongoDB Atlas
products_collection = app_db.products  # products is the name of the collection inside the database

from app import routes