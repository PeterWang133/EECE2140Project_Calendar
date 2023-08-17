import unittest
from object.c_time import CalendarTIme
import datetime

class TestClaendarTIme(unittest.TestCase):
    date_time = datetime.datetime(year=2023,month=5,day=1,hour=10,minute=30,second=0)
    test_d_t = CalendarTIme(date_time)
    def test_weekday(self):
        self.assertEqual(self.test_d_t.weekday_lst(),'Monday')
    def test_month(self):
        self.assertEqual(self.test_d_t.month_lst(),'May')
    def test_str(self):
        self.assertEqual(self.test_d_t.__str__(),'Date and Time: 05-01-2023 10:30')