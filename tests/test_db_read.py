import unittest
from pymongo import MongoClient
from app import client

class TestDatabaseRead(unittest.TestCase):
    def test_mongodb_connection(self):
        # Ping the MongoDB server
        self.assertTrue(client.admin.command('ping')['ok'], "MongoDB connection failed")

if __name__ == "__main__":
    unittest.main()
