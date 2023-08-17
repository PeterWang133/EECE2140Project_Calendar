import unittest
from object.c_eventlibrary import EventLibrary
from object.c_arrange import CalendarArrangement
from object.c_meeting import CalenderMeeting
from object.c_task import CalendarTask
from object.c_deadline import CalendarDeadline
import datetime

class TestEventLibrary(unittest.TestCase):
    date_time_1 = datetime.datetime(year=2023,month=8,day=13,hour=9,minute=35,second=0)
    date_time_2 = datetime.datetime(year=2023,month=8,day=15,hour=14,minute=40,second=0)
    test_library = EventLibrary()
    test_arrange = CalendarArrangement(date_time_2, 'Check test sample', False, 'Hourly')
    test_task = CalendarTask(date_time_1,'Pick up kids', datetime.timedelta(hours=1))
    test_meeting = CalenderMeeting(date_time_2, 'Project kickoff meeting', False, '')
    test_deadline = CalendarDeadline(date_time_2, 'Final is coming up', False)


    test_library.event_dict = {date_time_2:[test_arrange,test_deadline], date_time_1:[test_task]}
    
    def test_add_event(self):
        test_event = self.test_library.event_dict[self.date_time_2]
        s_1 = 'Arrangement\nDate and Time: 08-15-2023 14:40\nReminder: off\nEvent Description: Check test sample\nRecurs every hour.\n'
        self.assertEqual(test_event[0].__str__(), s_1)
        self.test_library.add_event(self.date_time_2,self.test_meeting)
        self.assertEqual(self.test_library.event_dict[self.date_time_2][2].__str__(), self.test_meeting.__str__())
    
    def test_del_event(self):
        s = ''
        self.test_library.del_event(self.date_time_2,self.test_deadline)
        for e in self.test_library.event_dict[self.date_time_2]:
            s += e.__str__()
        s_test = 'Arrangement\nDate and Time: 08-15-2023 14:40\nReminder: off\nEvent Description: Check test sample\nRecurs every hour.\n'
        self.assertEqual(s, s_test)
    
    def test_create_arrangement(self):
        """Tests two parts
        1) The method generates correct number of objects
        2) Each object has its own distinct time and date attribute
        """
        start = datetime.datetime(year=2023,month=8,day=15,hour=0,minute=0,second=0)
        time = self.test_arrange.date_time
        interval = datetime.timedelta(hours=1)
        end = datetime.datetime(year=2023,month=8,day=15,hour=23,minute=59,second=59)
        arrange_dict = self.test_library.create_arrangement(self.test_arrange, start, end)
        self.assertEqual(len(arrange_dict), 9) # Correct number of objects
        for d_t in arrange_dict:
            time = time+interval
            self.assertEqual(d_t, time) #Correct date and time for each generated object
        
    def test_sort_by_date(self):
        """Checks if the date is arranged in correct order"""
        test_dict = self.test_library.sort_by_date()
        date_lst = [self.date_time_1,self.date_time_2]
        i=0
        for d_t in test_dict:
            self.assertEqual(d_t, date_lst[i])
            i=i+1
        
        # Test the reverse case
        test_dict_2 = self.test_library.sort_by_date(True)
        date_lst = [self.date_time_2,self.date_time_1]
        i=0
        for d_t in test_dict_2:
            self.assertEqual(d_t, date_lst[i])
            i=i+1
    
    def test_sort_by_alphabet(self):
        expected_lst = [self.test_arrange, self.test_deadline, self.test_task]
        reverse_expected_lst = [self.test_task, self.test_deadline, self.test_arrange]
        expected = self.test_library.sort_by_alphabet()
        i = 0
        for lst in expected:
            self.assertEqual(lst[1].__str__(), expected_lst[i].__str__())
            i+=1
        
        # Test the reverse case
        expected_reverse = self.test_library.sort_by_alphabet(True)
        i = 0
        for lst in expected_reverse:
            self.assertEqual(lst[1].__str__(), reverse_expected_lst[i].__str__())
            i+=1
    
    def test_get_event_by_keyword(self):
        keyword = 'i'
        expected_lst = [self.test_deadline, self.test_task]
        keyword_dict = self.test_library.get_event_by_keyword(keyword)
        i = 0
        for d_t in keyword_dict:
            for e in keyword_dict[d_t]:
                self.assertEqual(e.__str__(), expected_lst[i].__str__())
                i+=1
    
    def test_get_date_event(self):
        test_dict = self.test_library.get_date_event(self.date_time_2)
        expected_lst = [[self.test_arrange, self.test_deadline]]
        i = 0
        for d_t in test_dict:
            for e in test_dict[d_t]:
                self.assertEqual(e.__str__(), expected_lst[i].__str__())
                i+=1
    
    def test_get_date_range(self):
        start = datetime.datetime(year=2023,month=8,day=15,hour=14,minute=40,second=0)
        end = datetime.datetime(year=2023,month=8,day=15,hour=16,minute=50,second=0)
        test_arrange_1 = CalendarArrangement(start+datetime.timedelta(hours=1), self.test_arrange.event_details,self.test_arrange.reminder, self.test_arrange.recurring)
        test_arrange_2 = CalendarArrangement(start+datetime.timedelta(hours=2), self.test_arrange.event_details,self.test_arrange.reminder, self.test_arrange.recurring)
        expected_lst = [self.test_arrange,self.test_deadline,test_arrange_1,test_arrange_2]
        date_range_dict = self.test_library.get_date_range(start,end)
        
        i = 0
        for d_t in date_range_dict:
            for e in date_range_dict[d_t]:
                self.assertEqual(e.__str__(), expected_lst[i].__str__())
                i+=1
    
    def test_get_event_by_type(self):
        expected_type = CalendarTask
        event_dict = self.test_library.get_event_by_type(expected_type)
        for d_t in event_dict:
            for e in event_dict[d_t]:
                self.assertIsInstance(e, expected_type)
    
    def test_get_date_range_obj(self):
        start = datetime.datetime(year=2023,month=8,day=13,hour=0,minute=0,second=0)
        end = datetime.datetime(year=2023,month=8,day=14,hour=23,minute=59,second=59)
        event_dict = self.test_library.get_date_range_obj(start,end)
        expected_obj = CalendarTask
        for d_t in event_dict:
            for e in event_dict[d_t]:
                self.assertIsInstance(e, expected_obj)
    
    def test_display_all_events(self):
        expected_s = self.test_arrange.__str__()+'\n'+self.test_deadline.__str__()+'\n'+self.test_task.__str__()+'\n'
        self.assertEqual(self.test_library.display_all_events(),expected_s)