import unittest
from app import app


class TestRoutes(unittest.TestCase):
    def setUp(self):
        # set up the test client
        self.app = app.test_client()
        self.app.testing = True

    # test route index - status code
    def test_index_status_code(self):
        # Send a GET request to the index route
        response = self.app.get("/index")

        # Check for the 200 in the response
        # assertEqual checks if the value that we are getting is equal to the expected value
        self.assertEqual(response.status_code, 200)

    # test route index - data
    def test_index_data(self):
        # Send a GET request to the index route
        response = self.app.get("/index")

        # Check for response data
        self.assertEqual(response.data.decode('utf-8'), "This is an awesome app!")