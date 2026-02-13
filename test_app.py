import unittest
from app import get_message

class TestApp(unittest.TestCase):
    def test_message(self):
        # This is the assertion (the test)
        self.assertEqual(get_message(), "Hello, DevOps!")

if __name__ == '__main__':
    unittest.main()