import unittest
from object.c_meeting import CalenderMeeting
import datetime

class TestCalendarMeeting(unittest.TestCase):
    date_time = datetime.datetime(year=2023,month=8,day=13,hour=9,minute=35,second=0)
    current_time = datetime.datetime(year=2023,month=8,day=13,hour=9,minute=30,second=0)
    test_meeting_1 = CalenderMeeting(date_time, 'Meeting with Luke', datetime.timedelta(minutes=10), 'https://zoom.us/')
    test_meeting_2 = CalenderMeeting(date_time, 'Project kickoff meeting', False, '')

    def test_reminder_for_meeting(self):
        self.assertTrue(self.test_meeting_1.reminder_for_meeting(self.current_time))
        self.assertFalse(self.test_meeting_2.reminder_for_meeting(self.current_time))
    
    def test_str_(self):
        s_1 = 'Meeting\nDate and Time: 08-13-2023 09:35\nReminder: 0:10:00 before the event\nEvent Description: Meeting with Luke\nLink: https://zoom.us/\n'
        s_2 = 'Meeting\nDate and Time: 08-13-2023 09:35\nReminder: off\nEvent Description: Project kickoff meeting\n'
        self.assertEqual(self.test_meeting_1.__str__(), s_1)
        self.assertEqual(self.test_meeting_2.__str__(), s_2)
    
    def test_write_to_file(self):
        s_1 = 'Meeting 2023-08-13 09:35:00 Meeting with Luke 08-13-2023,09:25:00 https://zoom.us/'
        s_2 = 'Meeting 2023-08-13 09:35:00 Project kickoff meeting False empty'
        self.assertEqual(self.test_meeting_1.write_to_file(), s_1)
        self.assertEqual(self.test_meeting_2.write_to_file(), s_2)