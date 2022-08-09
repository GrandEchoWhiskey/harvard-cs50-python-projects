from seasons import BirthDate
import unittest
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

class TestSum(unittest.TestCase):

    def test_one_year_ago(self):
        bd = BirthDate(str(date.today()-relativedelta(years=1)))
        self.assertEqual(str(bd), "Five hundred twenty-five thousand, six hundred minutes")

    def test_two_years_ago(self):
        bd = BirthDate(str(date.today()-relativedelta(years=2)))
        self.assertEqual(str(bd), "One million, fifty-one thousand, two hundred minutes")

    def test_invalid_date(self):
        self.assertRaises(SystemExit, BirthDate, "1NV4-L1-D")
        self.assertRaises(SystemExit, BirthDate, "2000-12-32")
        self.assertRaises(SystemExit, BirthDate, "1 January 2001")

if __name__ == '__main__':
    unittest.main()