import datetime
from object.c_event import CalendarEvent
from object.c_arrange import CalendarArrangement

class EventLibrary:
    def __init__(self) -> None:
        # {#datetime: [#list_of_events]}
        self.event_dict = {}

    def add_event(self, date_time, event):
        if date_time in self.event_dict:
            self.event_dict[date_time].append(event)
        else:
            self.event_dict[date_time]=[event]
        return self.event_dict
    
    def del_event(self, date_time, event):
        if event in self.event_dict[date_time]:
            self.event_dict[date_time].remove(event)
            if len(self.event_dict[date_time]) == 0:
                del self.event_dict[date_time]

    def create_arrangement(self, arrange:CalendarArrangement, start, end):
        arrange_dict = {}
        timestamp = arrange.change_time(arrange.date_time)
        while timestamp<=end:
            if arrange.remind_event(timestamp) and start.date()<=timestamp.date():
                arrange_dict[timestamp] = [CalendarArrangement(timestamp,arrange.event_details,arrange.reminder, arrange.recurring)]
            timestamp = arrange.change_time(timestamp)
        return arrange_dict

    def sort_by_date(self, reverse=False):
        sort_dict = {k:v for k, v in sorted(self.event_dict.items(), key=lambda x: x[0], reverse=reverse)}
        return sort_dict
    
    def sort_by_alphabet(self, reverse=False):
        alp_lst = []
        for d_t in self.event_dict:
            for e in self.event_dict[d_t]:
                alp_lst.append([d_t,e])
        alp_lst = sorted(alp_lst, key = lambda x:x[1].event_details)
        return alp_lst
    
    def get_event(self, event:CalendarEvent):
        for date_time in self.event_dict:
            for e in self.event_dict[date_time]:
                if e.date_time == event.date_time and e.event_details == event.event_details:
                    return e
        return 'Cannot find the event.'
    
    def get_event_by_keyword(self, keyword):
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
        date_event={}
        for d_t in self.event_dict:
            if d_t.date() == date:
                date_event[d_t] = self.event_dict[d_t]
        return date_event

    def get_date_range(self, start_date, end_date):
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
        s = ''
        for d_t in self.event_dict:
            for e in self.event_dict[d_t]:
                s+=e.__str__()+'\n'
        return s
    
    def save_file(self):
        pass

    def read_file(self):
        pass
    
