import datetime
import tkinter as tk
from object.c_eventlibrary import EventLibrary
from object.c_task import CalendarTask
from object.c_deadline import CalendarDeadline
from object.c_arrange import CalendarArrangement
from object.c_meeting import CalenderMeeting
from gui.c_main_menu import HomeScreen

events = EventLibrary()
d = datetime.datetime.today()
d_cal = d + datetime.timedelta(minutes=0)
d_3 = datetime.datetime(year=2023, month=8,day=8,hour=9,minute=0,second=0)
d_2 = datetime.datetime(year=2023, month=9, day=3, hour=4, minute=4, second=0)
d_4 = d+datetime.timedelta(minutes=5)
d_task = CalendarTask(d, 'Clean dishes', False)
obj = CalendarArrangement
d_deadline = CalendarDeadline(d_2, 'Final is coming up!')
d_arrangement = obj(d, 'Take pill', False, 'Daily')
d_task_2=CalendarTask(d_4,'Take kids back home', False)
d_task = CalendarTask(d_3,'Buy grocery', False)
d_meeting = CalenderMeeting(d_4,'Meeting with Kyle', False,'www.Apple.com')

events.add_event(d_task.date_time,d_task)
events.add_event(d,d_arrangement)
events.add_event(d_deadline.date_time, d_deadline)
events.add_event(d_task_2.date_time,d_task_2)

root = tk.Tk()

h = HomeScreen(root,events)

root.mainloop()