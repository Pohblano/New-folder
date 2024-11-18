# test_main.py
import unittest
from main import greet_person

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(greet_person('Alberto'), "Hello, Alberto!")

if __name__ == '__main__':
    unittest.main()
    