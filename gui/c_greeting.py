import datetime
import tkinter as tk
from object.c_deadline import CalendarDeadline
from object.c_eventlibrary import EventLibrary
import object.c_calendar as c_calendar
from object.c_meeting import CalenderMeeting
from object.c_arrange import CalendarArrangement
from object.c_task import CalendarTask

#Greeting message: Hello! ... Date today... Event today ... Any upcoming Deadline or early notification set by user

class Greeting(tk.Frame):
    def __init__(self,parent,obj:EventLibrary) -> None:
        super().__init__(parent)
        self.obj = obj
        self.greeting_label = tk.Label()
        self.now = datetime.datetime.today()
        self.greeting_label ['text'] = self.greeting_message(self.now)
        self.event_label = tk.Text()
        self.event_label.insert(tk.END, self.event_message(self.now))
        self.greeting_label.pack()
        self.event_label.pack()
        self.greeting_label.after(1000,self.update_time)
        self.event_label.after(10000, self.update_event)
    
    def greeting_message(self, now):
        s = f'Today is {now.date().strftime("%m-%d-%Y")}. It is now {now.time().strftime("%H:%M:%S")}.\n'
        return s

    def event_message(self, now):
        s = self.upcoming_deadline(now)+self.upcoming_event(now)
        return s

    def upcoming_deadline(self,now:datetime):
        today = now.date().strftime("%m-%d-%Y")
        future_time = (now+datetime.timedelta(days=10))
        future_time = future_time.date().strftime("%m-%d-%Y")
        s = c_calendar.search_and_sort(self.obj, [today, future_time], CalendarDeadline,'', False)
        if s=='':
            return 'No upcoming deadlines within the following 10 days.\n'
        return 'Important Notice\n'+s

    def upcoming_event(self,today:datetime):
        today = today.date().strftime("%m-%d-%Y")
        s = c_calendar.search_and_sort(self.obj, [today, today], CalendarTask,'', False)
        s += c_calendar.search_and_sort(self.obj, [today, today], CalendarArrangement,'', False)
        s +=c_calendar.search_and_sort(self.obj, [today, today], CalenderMeeting,'', False)
        if s=='':
            return 'No event today.\n'
        return 'Event today\n'+s

    def update_time(self):
        now = datetime.datetime.today()
        self.greeting_label.configure(text=self.greeting_message(now))
        self.greeting_label.after(1000,self.update_time)
    
    def upcoming_meeting(self, meeting:CalenderMeeting):
        now = datetime.datetime.today()

    def update_event(self):
        self.event_label.configure(state='normal')
        now = datetime.datetime.today()
        s=self.event_message(now)
        s_old = self.event_label.get('1.0', tk.END)
        s_old = ''.join(s_old.split())
        if s_old != s:
            self.event_label.replace('1.0',tk.END,s)
        self.event_label.configure(state='disabled')
        self.greeting_label.after(10000,self.update_event)



        