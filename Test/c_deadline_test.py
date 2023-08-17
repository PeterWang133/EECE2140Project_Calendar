import unittest
from object.c_deadline import CalendarDeadline
import datetime

class TestCalendarDeadline(unittest.TestCase):
    date_time_1 = datetime.datetime(year=2023,month=8,day=13,hour=9,minute=35,second=0)
    date_time_2 = datetime.datetime(year=2023,month=8,day=26,hour=14,minute=40,second=0)
    current_time = datetime.datetime(year=2023,month=8,day=17,hour=14,minute=40,second=0)
    test_deadline_1 = CalendarDeadline(date_time_1, 'Tuition Payment Due', False)
    test_deadline_2 = CalendarDeadline(date_time_2, 'Final is coming up', False)

    def test_count_down(self):
        self.assertEqual(self.test_deadline_1.count_down(self.current_time), 4)
        self.assertEqual(self.test_deadline_2.count_down(self.current_time), -9)
    
    def test_str(self):
        s_1 = 'Deadline\nDate and Time: 08-13-2023 09:35\nReminder: off\nEvent Description: Tuition Payment Due\n4 day(s) has passed.\n'
        s_2 = 'Deadline\nDate and Time: 08-26-2023 14:40\nReminder: off\nEvent Description: Final is coming up\n9 day(s) left.\n'
        self.assertEqual(self.test_deadline_1.__str__(), s_1)
        self.assertEqual(self.test_deadline_2.__str__(), s_2)
    
    def test_write_to_file(self):
        s_1 = 'Deadline 2023-08-13 09:35:00 Tuition Payment Due False'
        s_2 = 'Deadline 2023-08-26 14:40:00 Final is coming up False'
        self.assertEqual(self.test_deadline_1.write_to_file(), s_1)
        self.assertEqual(self.test_deadline_2.write_to_file(), s_2)