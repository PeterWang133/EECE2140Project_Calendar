import unittest
from object.c_eventlibrary import EventLibrary
from object.c_arrange import CalendarArrangement
from object.c_meeting import CalenderMeeting
from object.c_task import CalendarTask
from object.c_deadline import CalendarDeadline
import object.c_calendar as c_calendar
import datetime

class TestCalendar(unittest.TestCase):    
    date_time_1 = datetime.datetime(year=2023,month=8,day=13,hour=9,minute=35,second=0)
    date_time_2 = datetime.datetime(year=2023,month=8,day=15,hour=14,minute=40,second=0)
    date_time_3 = datetime.datetime(year=2023,month=8,day=14,hour=9,minute=35,second=0)
    test_library = EventLibrary()
    test_arrange = CalendarArrangement(date_time_2, 'Check test sample', False, 'Hourly')
    test_task = CalendarTask(date_time_1,'Pick up kids', datetime.timedelta(hours=1))
    test_meeting = CalenderMeeting(date_time_3, 'Project kickoff meeting', False, '')
    test_deadline = CalendarDeadline(date_time_2, 'Final is coming up', False)

    test_library.event_dict = {date_time_2:[test_arrange,test_deadline], date_time_1:[test_task], date_time_3:[test_meeting]}

    def test_search_by_date(self):
        date = '08-13-2023'
        search_dict = c_calendar.search_by_date(self.test_library,date)
        expected_lst = [self.test_task]
        i = 0
        for d_t in search_dict:
            for e in search_dict[d_t]:
                self.assertEqual(e.__str__(), expected_lst[i].__str__())
                i+=1
    
    def test_search_by_daterange(self):
        start = datetime.datetime(year=2023,month=8,day=15,hour=14,minute=40,second=0)
        end = datetime.datetime(year=2023,month=8,day=15,hour=17,minute=50,second=0)
        test_arrange_1 = CalendarArrangement(start+datetime.timedelta(hours=1), self.test_arrange.event_details,self.test_arrange.reminder, self.test_arrange.recurring)
        test_arrange_2 = CalendarArrangement(start+datetime.timedelta(hours=2), self.test_arrange.event_details,self.test_arrange.reminder, self.test_arrange.recurring)
        test_arrange_3 = CalendarArrangement(start+datetime.timedelta(hours=3), self.test_arrange.event_details,self.test_arrange.reminder, self.test_arrange.recurring)
        test_arrange_4 = CalendarArrangement(start+datetime.timedelta(hours=4), self.test_arrange.event_details,self.test_arrange.reminder, self.test_arrange.recurring)
        test_arrange_5 = CalendarArrangement(start+datetime.timedelta(hours=5), self.test_arrange.event_details,self.test_arrange.reminder, self.test_arrange.recurring)
        test_arrange_6 = CalendarArrangement(start+datetime.timedelta(hours=6), self.test_arrange.event_details,self.test_arrange.reminder, self.test_arrange.recurring)
        test_arrange_7 = CalendarArrangement(start+datetime.timedelta(hours=7), self.test_arrange.event_details,self.test_arrange.reminder, self.test_arrange.recurring)
        test_arrange_8 = CalendarArrangement(start+datetime.timedelta(hours=8), self.test_arrange.event_details,self.test_arrange.reminder, self.test_arrange.recurring)
        test_arrange_9 = CalendarArrangement(start+datetime.timedelta(hours=9), self.test_arrange.event_details,self.test_arrange.reminder, self.test_arrange.recurring)
        
        expected_lst = [self.test_arrange,self.test_deadline,test_arrange_1,test_arrange_2, test_arrange_3, test_arrange_4, test_arrange_5,test_arrange_6,test_arrange_7,test_arrange_8,test_arrange_9]
        date_range_dict = c_calendar.search_by_daterange(self.test_library, '08-15-2023', '08-15-2023')
        i = 0
        for d_t in date_range_dict:
            for e in date_range_dict[d_t]:
                self.assertEqual(e.__str__(), expected_lst[i].__str__())
                i+=1
    
    def test_search_by_daterange_obj(self):
        date = '08-13-2023'
        search_dict = c_calendar.search_by_daterange_obj(self.test_library,date,date)
        expected_type = CalendarTask
        for d_t in search_dict:
            for e in search_dict[d_t]:
                self.assertIsInstance(e,expected_type)
        
    def test_search_by_type(self):
        expected_type = CalendarArrangement
        result = c_calendar.search_by_type(self.test_library, expected_type)
        for d_t in result:
            for e in result[d_t]:
                self.assertIsInstance(e,expected_type)
    
    def test_search_by_keyword(self):
        keyword = 'i'
        expected_lst = [self.test_deadline, self.test_task, self.test_meeting]
        keyword_dict = c_calendar.search_by_keyword(self.test_library,keyword)
        i = 0
        for d_t in keyword_dict:
            for e in keyword_dict[d_t]:
                self.assertEqual(e.__str__(), expected_lst[i].__str__())
                i+=1
    
    def test_search_and_sort(self):
        date_range = ['08-13-2023','08-14-2023']
        type = CalenderMeeting
        keyword = 'Pick'

        #Case 1
        expected_str = self.test_task.__str__()+'\n'+self.test_meeting.__str__()+'\n'
        result = c_calendar.search_and_sort(self.test_library,date_range,'','',False)
        self.assertEqual(result,expected_str)

        #Case 2
        date_range = ['08-13-2023','08-16-2023']
        keyword = 'i'
        expected_str=self.test_task.__str__()+'\n'+self.test_meeting.__str__()+'\n'+self.test_deadline.__str__()+'\n'
        result = c_calendar.search_and_sort(self.test_library,date_range,'',keyword,False)
        self.assertEqual(result,expected_str)

        #Case 3
        expected_str=self.test_meeting.__str__()+'\n'
        result = c_calendar.search_and_sort(self.test_library,date_range,type,keyword,False)
        self.assertEqual(result,expected_str)

        #Case 4
        t_1 = '2023-08-15 14:40:00\n'
        t_2 = '2023-08-13 09:35:00\n'
        t_3 = '2023-08-14 09:35:00\n'
        expected_str=t_1+self.test_deadline.__str__()+'\n'+t_2+self.test_task.__str__()+'\n'+t_3+self.test_meeting.__str__()+'\n'
        result = c_calendar.search_and_sort(self.test_library,date_range,'',keyword,True)
        self.assertEqual(result,expected_str)
    
    def test_search_and_sort_obj(self):
        date_range = ['08-13-2023','08-14-2023']
        type = CalenderMeeting

        #Case 1
        expected_lst = [self.test_task,self.test_meeting]
        result = c_calendar.search_and_sort_obj(self.test_library,date_range,'','')
        i=0
        for d_t in result:
            for e in result[d_t]:
                self.assertEqual(e.__str__(), expected_lst[i].__str__())
                i+=1

        #Case 2
        date_range = ['08-13-2023','08-16-2023']
        keyword = 'i'
        expected_lst=[self.test_deadline,self.test_task,self.test_meeting]
        result = c_calendar.search_and_sort_obj(self.test_library,date_range,'',keyword)
        i=0
        for d_t in result:
            for e in result[d_t]:
                self.assertEqual(e.__str__(), expected_lst[i].__str__())
                i+=1
        
        #Case 3
        #Case 3
        expected_lst=[self.test_meeting]
        result = c_calendar.search_and_sort_obj(self.test_library,date_range,type,keyword)
        i=0
        for d_t in result:
            for e in result[d_t]:
                self.assertEqual(e.__str__(), expected_lst[i].__str__())
                i+=1

