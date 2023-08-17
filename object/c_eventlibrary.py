import datetime
from object.c_event import CalendarEvent
from object.c_arrange import CalendarArrangement
from object.c_meeting import CalenderMeeting
from object.c_task import CalendarTask
from object.c_deadline import CalendarDeadline

import json

class EventLibrary:
    """An EventLibrary class that stores all of the CalendarEvent objects"""
    def __init__(self) -> None:
        """Initializes the EventLibrary obejct"""
        # {#datetime: [#list_of_events]}
        self.event_dict = {}

    def add_event(self, date_time, event):
        """Adds a CalendarEvent objecg into the event dictionary
        : param: self: an EventLibrary object, date_time: a datetime object, event: a CalendarEvent object
        : return: an updated event dictionary
        """
        if date_time in self.event_dict:
            self.event_dict[date_time].append(event)
        else:
            self.event_dict[date_time]=[event]
        return self.event_dict
    
    def del_event(self, date_time, event):
        """Deletes an event from the event dictionary
        : param self: an EventLibrary object, date_time: a datetime object, event: a CalendarEvent object
        : return: an updated event dictionary that deleted the input event
        """
        if event in self.event_dict[date_time]:
            self.event_dict[date_time].remove(event)
            if len(self.event_dict[date_time]) == 0:
                del self.event_dict[date_time]

    def create_arrangement(self, arrange:CalendarArrangement, start, end):
        """Creates a list of CalendarArrangement object that recurs within the date range
        set by a start date and an end date
        : param self: an EventLibrary object, arrange: a CalendarArrangement object, start: a datetime object, end: a datetime object
        reutrn: a dictionary that contains all of the CalendarArrangement objects that should recur within the date range
        """
        arrange_dict = {}
        timestamp = arrange.change_time(arrange.date_time)
        while timestamp<=end:
            if arrange.remind_event(timestamp) and start.date()<=timestamp.date():
                arrange_dict[timestamp] = [CalendarArrangement(timestamp,arrange.event_details,arrange.reminder, arrange.recurring)]
            timestamp = arrange.change_time(timestamp)
        return arrange_dict

    def sort_by_date(self, reverse=False):
        """Sorts the events in order of date and time
        : param self: an EventLibrary object, reverse: a Boolean
        : return: a dictionary with all events being arranged in order of date and time
        """
        sort_dict = {k:v for k, v in sorted(self.event_dict.items(), key=lambda x: x[0], reverse=reverse)}
        return sort_dict
    
    def sort_by_alphabet(self, reverse=False):
        """Sorts the events in order of alphabets
        : param self: an EventLibrary object, reverse: a Boolean
        : return: a list with all events being arranged in order of alphabets
        """
        alp_lst = []
        for d_t in self.event_dict:
            for e in self.event_dict[d_t]:
                alp_lst.append([d_t,e])
        alp_lst = sorted(alp_lst, key = lambda x:x[1].event_details,reverse=reverse)
        return alp_lst
    
    def get_event_by_keyword(self, keyword):
        """Search the events with the event details matching with the keyword
        : param self: an EventLibrary object, keyword: a String
        return: an event dictionary with all of the events that have the event details matching with the keyword
        """
        keyword_dict={}
        for date_time in self.event_dict:
            for e in self.event_dict[date_time]:
                if keyword in e.event_details:
                    if date_time in keyword_dict:
                        keyword_dict[date_time].append(e)
                    else:
                        keyword_dict[date_time] = [e]
        return keyword_dict
    
    def get_date_event(self, date):
        """Search the events by date
        This method generates CalendarArrangement object that has recurring dates with in the searched date range
        : param self: an EventLibrary object, date: a datetime object
        : return: an event dictionary with the event of the searched date
        """
        date_event={}
        for d_t in self.event_dict:
            if d_t.date() == date:
                date_event[d_t] = self.event_dict[d_t]
        return date_event

    def get_date_range(self, start_date, end_date):
        """Search the events by date range
        This method generates CalendarArrangement object that has recurring dates with in the searched date range
        : param self: an EventLibrary object, start_date: a datetime object, end_date: a datetime object
        : return: an event dictionary with the event of the searched date range
        """
        date_event = {}
        arrange={}
        for d_t in self.event_dict:
            if d_t.date()>=start_date.date() and d_t.date()<=end_date.date():
                date_event[d_t] = self.event_dict[d_t]
        for d_t in self.event_dict:
            for e in self.event_dict[d_t]:
                if isinstance(e, CalendarArrangement) and e.recurring!='None':
                    arrange = self.create_arrangement(e, start_date, end_date)
            for d_t in arrange:
                    if d_t in date_event:
                        date_event[d_t].append(arrange[d_t][0])
                    else:
                        date_event[d_t] = arrange[d_t]
            arrange = {}
        return date_event
    
    def get_event_by_type(self, event_type):
        """Search the events by event type
        : param self: an EventLibrary object, event_type: an object
        : return: an event dictionary with the matching event type
        """
        type_event={}
        for d_t in self.event_dict:
            for e in self.event_dict[d_t]:
                if isinstance(e,event_type):
                    if d_t in type_event:
                        type_event[d_t].append(e)
                    else:
                        type_event[d_t] = [e]
        return type_event

    def get_date_range_obj(self, start_date, end_date):
        """Search the events by date range
        This method does not generate multiple CalendarArrangement object, but only saves the original 
        CalendarArrangement object if that object has a recurring date within the date range
        : param self: an EventLibrary object, start_date: a datetime object, end_date: a datetime object
        : return: an event dictionary with the event of the searched date range
        """
        date_event = {}
        for d_t in self.event_dict:
            for e in self.event_dict[d_t]:
                if e.date_time.date()>=start_date.date() and e.date_time.date()<=end_date.date():
                    if d_t in date_event:
                        date_event[d_t].append(e)
                    else:
                        date_event[d_t] = [e]
                elif isinstance(e,CalendarArrangement) and e.recurring!='None' and e.check_recur(start_date,end_date):
                    if d_t in date_event:
                        date_event[d_t].append(e)
                    else:
                        date_event[d_t] = [e]
        return date_event

    def display_all_events(self):
        """Prints out the EventLibrary object
        : param self: an EventLibrary object
        : return: a String
        """
        s = ''
        for d_t in self.event_dict:
            for e in self.event_dict[d_t]:
                s+=e.__str__()+'\n'
        return s
    
    def save_file(self):
        """Saves the EventLibrary object into a text file
        : param self: an EventLibrary object
        : return: a text file that contains all the events from the EventLibrary object
        """
        with open('Calendar_events.txt', mode='w', encoding='utf8') as f:
            for d_t in self.event_dict:
                for e in self.event_dict[d_t]:
                    print(e.write_to_file(), file=f)

    def read_file(self):
        """Reads the lists of events from a text file
        : param self: an EventLibrary object
        : return: an EventLibrary loaded with CalendarEvent object
        """
        #Read the file
        with open('Calendar_events.txt', mode='r', encoding='utf8') as f:
            s = f.readlines()
        s = [i.split() for i in s]

        def write_meeting(lst):
            """Reads a list that contains information about a meeting event
            : param lst: a List
            : return: a CalendarMeeting object
            """
            date_time = lst[1]+' '+lst[2]
            date_time = datetime.datetime.strptime(date_time,"%Y-%m-%d %H:%M:%S")
            event_details = lst[3:-2]
            event_details = ' '.join(event_details)
            reminder = False
            if lst[-2] != 'False':
                reminder = lst[-2]
                reminder = datetime.datetime.strptime(reminder,"%m-%d-%Y,%H:%M:%S")
                reminder = date_time-reminder
            link = lst[-1]
            if link == 'empty':
                link=''
            return CalenderMeeting(date_time,event_details,reminder,link)    
        
        def write_arrangement(lst):
            """Reads a list that contains information about an arrangement event
            : param lst: a List
            : return: a CalendarArrangement object
            """
            date_time = lst[1]+' '+lst[2]
            date_time = datetime.datetime.strptime(date_time,"%Y-%m-%d %H:%M:%S")
            event_details = lst[3:-2]
            event_details = ' '.join(event_details)
            reminder = False
            if lst[-2] != 'False':
                reminder = lst[-2]
                reminder = datetime.datetime.strptime(reminder,"%m-%d-%Y,%H:%M:%S")
                reminder = date_time-reminder
            recurring = lst[-1]
            return CalendarArrangement(date_time,event_details,reminder,recurring)
        
        def write_task_or_deadline(lst):
            """Reads a list that contains information about a deadline or task event
            : param lst: a List
            : return: a CalendarTask object or a CalendarDeadline object
            """
            date_time = lst[1]+' '+lst[2]
            date_time = datetime.datetime.strptime(date_time,"%Y-%m-%d %H:%M:%S")
            event_details = lst[3:-1]
            event_details = ' '.join(event_details)
            reminder = False
            if lst[-1] != 'False':
                reminder = lst[-1]
                reminder = datetime.datetime.strptime(reminder,"%m-%d-%Y,%H:%M:%S")
                reminder = date_time-reminder
            if lst[0] == 'Task':
                return CalendarTask(date_time,event_details,reminder)
            elif lst[0] == 'Deadline':
                return CalendarDeadline(date_time,event_details,reminder)
        if s!=[]:
            for event in s:
                obj = ''
                if event[0] == 'Arrangement':
                    obj = write_arrangement(event)
                elif event[0] == 'Meeting':
                    obj=write_meeting(event)
                else:
                    obj=write_task_or_deadline(event)
                self.add_event(obj.date_time,obj)

        

    
