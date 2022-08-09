from um import count
import unittest

class TestSum(unittest.TestCase):

    def test_single(self):
        self.assertEqual(count('um'), 1)

    def test_single_quote(self):
        self.assertEqual(count('um?'), 1)

    def test_sentence(self):
        self.assertEqual(count('Um, thanks for the album.'), 1)

    def test_sentence_2(self):
        self.assertEqual(count('Um, thanks, um...'), 2)


if __name__ == '__main__':
    unittest.main()
    