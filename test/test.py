import unittest
from src.main import *

class TestAdd(unittest.TestCase):
    """test main.py add
    """

    def test_add(self):
        a = 2
        b = 3
        expected = 5
        actual = add(a,b)
        self.assertEqual(expected, actual)

    def test_add_alt(self):
        self.assertEqual(13, 7 + 6)


if __name__ == "__main__":
   unittest.main()

