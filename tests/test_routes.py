import unittest
from app import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_invalid_method(self):
        # Send a POST request to a route that only accepts GET
        response = self.app.post('/')
        self.assertEqual(response.status_code, 405)  # Method Not Allowed
        self.assertIn(b'METHOD NOT ALLOWED', response.data.upper())  # Optional: Check response content

if __name__ == "__main__":
    unittest.main()
