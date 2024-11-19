import unittest
from app import db

class TestDatabaseWrite(unittest.TestCase):
    def setUp(self):
        self.test_collection = db['test_collection']

    def tearDown(self):
        # Clean up the test collection
        self.test_collection.delete_many({})

    def test_insert_document(self):
        # Insert a test document
        test_document = {"name": "Test Product", "price": 10.99}
        result = self.test_collection.insert_one(test_document)

        # Verify the document was inserted
        inserted_doc = self.test_collection.find_one({"_id": result.inserted_id})
        self.assertIsNotNone(inserted_doc)
        self.assertEqual(inserted_doc["name"], "Test Product")
        self.assertEqual(inserted_doc["price"], 10.99)

if __name__ == "__main__":
    unittest.main()
