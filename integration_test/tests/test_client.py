import unittest
from client import Client


class ClientTestCase(unittest.TestCase):

    def test_with_redis(self):
        client = Client()
        client.set('tomato', 2)
        self.assertEqual(2, int(client.get('tomato')))
