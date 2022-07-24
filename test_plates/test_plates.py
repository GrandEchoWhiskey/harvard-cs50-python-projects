from plates import is_valid
import unittest

class TestSum(unittest.TestCase):

    def test_ok(self):
        self.assertEqual(is_valid('CS50'), True, "Plate should be ok")

    def test_too_long(self):
        self.assertEqual(is_valid("helloworld"), False, "Plate should be shorter than 6 letters and digits")

    def test_too_short(self):
        self.assertEqual(is_valid("H"), False, "Plate should be longer than 1 letter and digits")

    def test_starting_number(self):
        self.assertEqual(is_valid("H2"), False, "Plate should start with 2 letters")

    def test_letter_after_number(self):
        self.assertEqual(is_valid("HA2X"), False, "Plate should end with digits")

    def test_symbols(self):
        self.assertEqual(is_valid("CS-50"), False, "Plate should only contain letters, and digits")

    def test_zero_placement(self):
        self.assertEqual(is_valid("CS050"), False, "Plate numbers should not start with 0")

if __name__ == '__main__':
    unittest.main()