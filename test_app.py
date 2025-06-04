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



def test_not_found(self):
    response = self.client.get('/rota-que-nao-existe')
    self.assertEqual(response.status_code, 404)

def test_login_falha(self):
    response = self.client.post('/login', json={"username": "", "password": ""})
    self.assertEqual(response.status_code, 400)
    self.assertIn("error", response.json)

def test_protected_without_token(self):
    response = self.client.get('/protected')
    self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()