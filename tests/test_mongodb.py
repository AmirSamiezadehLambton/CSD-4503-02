import unittest
from pymongo import MongoClient
from dotenv import load_dotenv
import os


class TestDB(unittest.TestCase):
    def setUp(self):
        load_dotenv()

        db_username = os.environ["MONGODB_USERNAME"]
        db_password = os.environ["MONGODB_PASSWORD"]

        # set up the test client
        self.client = MongoClient(f"mongodb+srv://{db_username}:{db_password}@cluster0.ktsh8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

    def test_connection(self):
        # self.client.<database_name>.command('ping')
        response = self.client.app.command('ping')
        print(response)


    # # test route
