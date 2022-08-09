from working import convert
import unittest

class TestSum(unittest.TestCase):

    def test_no_minutes(self):
        self.assertEqual(convert('9 AM to 5 PM'), "09:00 to 17:00")

    def test_minutes(self):
        self.assertEqual(convert('9:00 AM to 5:00 PM'), "09:00 to 17:00")

    def test_pmam_no_minutes(self):
        self.assertEqual(convert('10 PM to 8 AM'), "22:00 to 08:00")

    def test_pmam_minutes(self):
        self.assertEqual(convert('10:30 PM to 8:50 AM'), "22:30 to 08:50")

    def test_not_minutes(self):
        self.assertRaises(ValueError, convert, "9:60 AM to 5:60 PM")

    def test_wrong_separator(self):
        self.assertRaises(ValueError, convert, "9 AM - 5 PM")

    def test_wrong_separator_long(self):
        self.assertRaises(ValueError, convert, "9:00 AM - 17:00 PM")

if __name__ == '__main__':
    unittest.main()
    