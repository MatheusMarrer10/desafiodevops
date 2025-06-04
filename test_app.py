import unittest
from app import app
import werkzeug
werkzeug
if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()



def test_home(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
    self.assertNotEqual(response.json, {"message": "API is down"})

def test_get_items(self):
    response = self.client.get('/items')
    self.assertEqual(response.status_code, 200)
    self.assertIsInstance(response.json['items'], list)

def test_login(self):
    response = self.client.post('/login')
    self.assertEqual(response.status_code, 200)
    self.assertTrue('access_token' in response.json)

if __name__ == '__main__':
    unittest.main()