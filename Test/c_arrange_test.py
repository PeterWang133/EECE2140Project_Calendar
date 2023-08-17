import unittest
from object.c_arrange import CalendarArrangement

import datetime

class TestCalendarArrangement(unittest.TestCase):
    date_time_1 = datetime.datetime(year=2023,month=8,day=13,hour=9,minute=35,second=0)
    date_time_2 = datetime.datetime(year=2023,month=8,day=15,hour=14,minute=40,second=0)
    test_arrange_1 = CalendarArrangement(date_time_1,'Yoga class',False,'Weekly')
    test_arrange_2 = CalendarArrangement(date_time_2, 'Take pill', datetime.timedelta(minutes=5), 'Daily')
    test_arrange_3 = CalendarArrangement(date_time_1, 'Rebecca\'s Birthday', datetime.timedelta(days=1), 'Yearly')
    test_arrange_4 = CalendarArrangement(date_time_2, 'Check test sample', False, 'Hourly')
    test_arrange_5 = CalendarArrangement(date_time_1, 'Dinner with S', datetime.timedelta(hours=2), 'None')
    test_arrange_6 = CalendarArrangement(date_time_2, 'Attend Discussion Board', False, 'Monthly')

    def test_remind_hourly(self):
        current_time_1 = datetime.datetime(year=2023,month=9,day=13,hour=14,minute=40,second=0)
        current_time_2 = datetime.datetime(year=2023,month=8,day=15,hour=14,minute=50,second=0)
        self.assertTrue(self.test_arrange_4.remind_hourly(current_time_1))
        self.assertFalse(self.test_arrange_4.remind_hourly(current_time_2))
    
    def test_remind_daily(self):
        current_time_1 = datetime.datetime(year=2023,month=9,day=16,hour=14,minute=40,second=0)
        current_time_2 = datetime.datetime(year=2023,month=8,day=15,hour=15,minute=40,second=0)
        self.assertTrue(self.test_arrange_2.remind_daily(current_time_1))
        self.assertFalse(self.test_arrange_2.remind_daily(current_time_2))
        
    def test_remind_weekly(self):
        current_time_1 = datetime.datetime(year=2023,month=8,day=20,hour=9,minute=35,second=0)
        current_time_2 = datetime.datetime(year=2023,month=8,day=23,hour=9,minute=35,second=0)
        self.assertTrue(self.test_arrange_1.remind_weekly(current_time_1))
        self.assertFalse(self.test_arrange_1.remind_weekly(current_time_2))
    
    def test_remind_monthly(self):
        current_time_1 = datetime.datetime(year=2023,month=10,day=15,hour=9,minute=35,second=0)
        current_time_2 = datetime.datetime(year=2023,month=11,day=30,hour=9,minute=35,second=0)
        self.assertTrue(self.test_arrange_6.remind_monthly(current_time_1))
        self.assertFalse(self.test_arrange_6.remind_monthly(current_time_2))
    
    def test_remind_yearly(self):
        current_time_1 = datetime.datetime(year=2024,month=8,day=13,hour=9,minute=35,second=0)
        current_time_2 = datetime.datetime(year=2023,month=8,day=20,hour=9,minute=35,second=0)
        self.assertTrue(self.test_arrange_3.remind_yearly(current_time_1))
        self.assertFalse(self.test_arrange_3.remind_yearly(current_time_2))
    
    def test_remind_event(self):
        current_time_1 = datetime.datetime(year=2024,month=8,day=13,hour=9,minute=35,second=0)
        current_time_2 = datetime.datetime(year=2023,month=8,day=20,hour=9,minute=35,second=0)
        self.assertFalse(self.test_arrange_1.remind_event(current_time_1))
        self.assertFalse(self.test_arrange_2.remind_event(current_time_2))
        self.assertTrue(self.test_arrange_3.remind_event(current_time_1))
        self.assertFalse(self.test_arrange_4.remind_event(current_time_2))
        self.assertFalse(self.test_arrange_5.remind_event(current_time_1))
        self.assertFalse(self.test_arrange_6.remind_event(current_time_2))
        
    def test_change_time(self):
        current_time = datetime.datetime(year=2023,month=8,day=13,hour=9,minute=35,second=0)
        self.assertEqual(self.test_arrange_1.change_time(current_time), datetime.datetime(year=2023,month=8,day=20,hour=9,minute=35,second=0))
        self.assertEqual(self.test_arrange_2.change_time(current_time), datetime.datetime(year=2023,month=8,day=14,hour=9,minute=35,second=0))
        self.assertEqual(self.test_arrange_3.change_time(current_time), datetime.datetime(year=2024,month=8,day=13,hour=0,minute=35,second=0))
        self.assertEqual(self.test_arrange_4.change_time(current_time), datetime.datetime(year=2023,month=8,day=13,hour=10,minute=35,second=0))
        self.assertEqual(self.test_arrange_5.change_time(current_time), 0)
        self.assertEqual(self.test_arrange_6.change_time(current_time), datetime.datetime(year=2023,month=9,day=15,hour=0,minute=40,second=0))
    
    def test_check_recur(self):
        start = datetime.datetime(year=2023,month=8,day=10,hour=14,minute=40,second=0)
        end = datetime.datetime(year=2023,month=8,day=16,hour=14,minute=40,second=0)
        self.assertTrue(self.test_arrange_1.check_recur(start,end))
        self.assertTrue(self.test_arrange_2.check_recur(start,end))
        self.assertTrue(self.test_arrange_3.check_recur(start,end))
        self.assertTrue(self.test_arrange_4.check_recur(start,end))
        self.assertTrue(self.test_arrange_6.check_recur(start,end))
    
    def test_str(self):
        s_1 = 'Arrangement\nDate and Time: 08-13-2023 09:35\nReminder: off\nEvent Description: Yoga class\nRecurs on every Sunday.\n'
        s_2 = 'Arrangement\nDate and Time: 08-15-2023 14:40\nReminder: 0:05:00 before the event\nEvent Description: Take pill\nRecurs Every day\n'
        s_3 = 'Arrangement\nDate and Time: 08-13-2023 09:35\nReminder: 1 day, 0:00:00 before the event\nEvent Description: Rebecca\'s Birthday\nRecurs on August 13 every year.\n'
        s_4 = 'Arrangement\nDate and Time: 08-15-2023 14:40\nReminder: off\nEvent Description: Check test sample\nRecurs every hour.\n'
        s_5 = 'Arrangement\nDate and Time: 08-13-2023 09:35\nReminder: 2:00:00 before the event\nEvent Description: Dinner with S\nDoes not recur.\n'
        s_6 = 'Arrangement\nDate and Time: 08-15-2023 14:40\nReminder: off\nEvent Description: Attend Discussion Board\nRecurs on 15 day of every month.\n'
        self.assertEqual(self.test_arrange_1.__str__(), s_1)
        self.assertEqual(self.test_arrange_2.__str__(), s_2)
        self.assertEqual(self.test_arrange_3.__str__(), s_3)
        self.assertEqual(self.test_arrange_4.__str__(), s_4)
        self.assertEqual(self.test_arrange_5.__str__(), s_5)
        self.assertEqual(self.test_arrange_6.__str__(), s_6)
    
    def test_write_to_file(self):
        s_1 = 'Arrangement 2023-08-13 09:35:00 Yoga class False Weekly '
        s_2 = 'Arrangement 2023-08-15 14:40:00 Take pill 08-15-2023,14:35:00 Daily '
        s_3 = 'Arrangement 2023-08-13 09:35:00 Rebecca\'s Birthday 08-12-2023,09:35:00 Yearly '
        s_4 = 'Arrangement 2023-08-15 14:40:00 Check test sample False Hourly '
        s_5 = 'Arrangement 2023-08-13 09:35:00 Dinner with S 08-13-2023,07:35:00 None '
        s_6 = 'Arrangement 2023-08-15 14:40:00 Attend Discussion Board False Monthly '
        self.assertEqual(self.test_arrange_1.write_to_file(), s_1)
        self.assertEqual(self.test_arrange_2.write_to_file(), s_2)
        self.assertEqual(self.test_arrange_3.write_to_file(), s_3)
        self.assertEqual(self.test_arrange_4.write_to_file(), s_4)
        self.assertEqual(self.test_arrange_5.write_to_file(), s_5)
        self.assertEqual(self.test_arrange_6.write_to_file(), s_6)
