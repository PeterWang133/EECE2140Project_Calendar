import unittest
from object.c_task import CalendarTask
import datetime

class TestCalendarTask(unittest.TestCase):
    date_time = datetime.datetime(year=2023,month=7,day=20,hour=15,minute=20,second=0)
    test_task_1 = CalendarTask(date_time, 'Wash dishes', False)
    test_task_2 = CalendarTask(date_time,'Pick up kids', datetime.timedelta(hours=1))

    def test_str(self):
        s_1 = 'Task\nDate and Time: 07-20-2023 15:20\nReminder: off\nEvent Description: Wash dishes\n'
        self.assertEqual(self.test_task_1.__str__(),s_1)

        s_2 = 'Task\nDate and Time: 07-20-2023 15:20\nReminder: 1:00:00 before the event\nEvent Description: Pick up kids\n'
        self.assertEqual(self.test_task_2.__str__(), s_2)
    
    def test_write_to_file(self):
        s_1 = 'Task 2023-07-20 15:20:00 Wash dishes False'
        self.assertEqual(self.test_task_1.write_to_file(),s_1)

        s_2 = 'Task 2023-07-20 15:20:00 Pick up kids 07-20-2023,14:20:00'
        self.assertEqual(self.test_task_2.write_to_file(), s_2)