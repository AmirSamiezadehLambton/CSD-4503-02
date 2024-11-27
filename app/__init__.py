# Run this command in the terminal to install flask framework:
# pip install flask

# To import the flask framework, we use:
from flask import Flask
from pymongo import MongoClient  # pip install pymongo
from dotenv import load_dotenv
import os
import sentry_sdk

load_dotenv()

db_username = os.environ["MONGODB_USERNAME"]
db_password = os.environ["MONGODB_PASSWORD"]
sentry_dsn = os.environ["SENTRY_DSN"]

sentry_sdk.init(
    dsn=sentry_dsn,
    traces_sample_rate=1.0,
    _experiments={
        # Set continuous_profiling_auto_start to True
        # to automatically start the profiler on when
        # possible.
        "continuous_profiling_auto_start": True,
    },
)
app = Flask(__name__)

# MongoDB Atlas Client
client = MongoClient(f"mongodb+srv://{db_username}:{db_password}@cluster0.ktsh8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

app_db = client.app  # app is the name of the database in MongoDB Atlas
products_collection = app_db.products  # products is the name of the collection inside the database

from app import routes