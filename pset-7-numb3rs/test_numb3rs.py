from numb3rs import validate
import unittest

class TestSum(unittest.TestCase):

    def test_localhost(self):
        self.assertTrue(validate("127.0.0.1"), "Localhost should return True")

    def test_broadcast(self):
        self.assertTrue(validate("255.255.255.255") or validate("192.168.1.255"), "Broadcast address should return True")

    def test_network(self):
        self.assertTrue(validate("0.0.0.0"), "Network address should return True")

    def test_host(self):
        self.assertTrue(validate("192.168.1.1"), "Host address should return True")

    def test_too_big(self):
        self.assertFalse(validate("512.512.512.512") or validate("1.2.3.1000"), "Too big for octets. 8bit -> 0-255")

    def test_string(self):
        self.assertFalse(validate("cat"), "IP can not contain strings")

    def test_first(self):
        self.assertFalse(validate("1000.2.3.4"), "Too big for octets. 8bit -> 0-255")

    def test_last(self):
        self.assertFalse(validate("192.168.1.256"), "Too big for octets. 8bit -> 0-255")

    def test_empty(self):
        self.assertFalse(validate("...."), "Octets can not be empty")

    def test_5o(self):
        self.assertFalse(validate("192.168.1.255.1") or validate("512.512.512.512.512"), "Too much octets")

    def test_3o(self):
        self.assertFalse(validate("192.168.1"), "Need 4 octets")

if __name__ == '__main__':
    unittest.main()
