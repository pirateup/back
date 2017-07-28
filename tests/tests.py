import unittest
from pirateup import pirateup

class PirateTestCase(unittest.TestCase):

    def setUp(self):
        pirateup.app.testing = True
        self.app = pirateup.app.test_client()

    def tearDown(self):
        pass

    def test_pirate_say_hello(self):
        resp = self.app.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, b'Hello')

if __name__ == '__main__':
    unittest.main()
