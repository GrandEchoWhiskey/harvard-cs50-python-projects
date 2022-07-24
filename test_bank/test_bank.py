from bank import value
import unittest

class TestSum(unittest.TestCase):

    def test_hello_lower(self):
        self.assertEqual(value("hello world"), 0, "Strings starting with hello should return 0")

    def test_other_h_lower(self):
        self.assertEqual(value("hi CS50"), 20, "Strings starting with H or h but not hello should return 20")

    def test_none_h_lower(self):
        self.assertEqual(value("nice to see you duck"), 100, "Strings not starting with H or h should return 100")

    def test_hello_upper(self):
        self.assertEqual(value("HeLlO wOrlD"), 0, "Strings starting with hello should return 0")

    def test_other_h_upper(self):
        self.assertEqual(value("Hi CS50"), 20, "Strings starting with H or h but not hello should return 20")

    def test_none_h_upper(self):
        self.assertEqual(value("Nice to see you Duck"), 100, "Strings not starting with H or h should return 100")

if __name__ == '__main__':
    unittest.main()