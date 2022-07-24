from twttr import shorten
import unittest

class TestSum(unittest.TestCase):

    def test_output(self):
        self.assertEqual(shorten("hll wrld"), "hll wrld", "Not working without changes")

    def test_lower(self):
        self.assertEqual(shorten("abcdefghijklmnopqrstuvwxyz"), "bcdfghjklmnpqrstvwxyz", "Lowercase aeiou not working correctly")

    def test_upper(self):
        self.assertEqual(shorten("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "BCDFGHJKLMNPQRSTVWXYZ", "Uppercase AEIOU not working correctly")

    def test_numbers(self):
        self.assertEqual(shorten("1 4M 4 NUMB3R 5TR1NG"), "1 4M 4 NMB3R 5TR1NG", "Numbers should be omitted")

    def test_punctuation(self):
        self.assertEqual(shorten("Hi I'm a CS50 student, a duck, and also a coder!"), "H 'm  CS50 stdnt,  dck, nd ls  cdr!", "Punctuation should be ommited")

if __name__ == '__main__':
    unittest.main()