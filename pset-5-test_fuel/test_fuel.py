from fuel import convert, gauge
import unittest

class TestSum(unittest.TestCase):

    def test_convert_ok(self):
        self.assertEqual(convert("1/4"), 25, "1/4 should return int(25) as percent")

    def test_convert_zero_division(self):
        self.assertRaises(ZeroDivisionError, convert, "1/0")

    def test_convert_value(self):
        self.assertRaises(ValueError, convert, "2/1")

    def test_gauge_str(self):
        self.assertEqual(gauge(50), "50%", "Function should return formated percent string")

    def test_gauge_E(self):
        self.assertEqual(gauge(1), "E", "Function should return E when below or equal 1%")

    def test_gauge_F(self):
        self.assertEqual(gauge(99), "F", "Function should return F when above or equal 99%")


if __name__ == '__main__':
    unittest.main()