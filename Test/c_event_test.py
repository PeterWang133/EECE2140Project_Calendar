import unittest
from object.c_event import CalendarEvent
import datetime

class TestCalendarEvent(unittest.TestCase):
    date_time = datetime.datetime(year=2023,month=5,day=1,hour=10,minute=30,second=0)
    test_event_1 = CalendarEvent(date_time,'Wake up', False)
    test_event_2 = CalendarEvent(date_time,'Wake up !!!', datetime.timedelta(minutes=10))
    new_time = datetime.datetime(year=2023,month=6,day=2,hour=8,minute=20,second=0)

    def test_notification(self):
        current_time = datetime.datetime(year=2023,month=5,day=1,hour=10,minute=20,second=0)
        self.assertFalse(self.test_event_1.notification(current_time))
        self.assertTrue(self.test_event_2.notification(current_time))
    
    def test_modify_event_details(self):
        test_event = CalendarEvent(self.date_time,'Wake up', False)
        test_event.modify_event_details('Go to sleep')
        self.assertEqual(test_event.event_details,'Go to sleep')
    
    def test_modify_datetime(self):
        test_event = CalendarEvent(self.date_time,'Wake up', False)
        test_event.modify_datetime(self.new_time)
        self.assertEqual(test_event.date_time, datetime.datetime(year=2023,month=6,day=2,hour=8,minute=20,second=0))
    
    def test_str(self):
       s_1 = 'Date and Time: 05-01-2023 10:30\nReminder: off\nEvent Description: Wake up'
       self.assertEqual(self.test_event_1.__str__(), s_1)

       s_2 = 'Date and Time: 05-01-2023 10:30\nReminder: 0:10:00 before the event\nEvent Description: Wake up !!!'
       self.assertEqual(self.test_event_2.__str__(), s_2)