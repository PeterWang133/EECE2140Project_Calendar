import tkinter as tk
from tkinter import messagebox
import webbrowser
import winsound

from object.c_eventlibrary import EventLibrary
from object.c_event import CalendarEvent
from object.c_meeting import CalenderMeeting

from windows_toasts import WindowsToaster, ToastText1

import datetime

class Notification():
    def __init__(self,obj:EventLibrary):
        self.object = obj
        self.noti_lst = []
        self.date_time = datetime.datetime.today()
        self.d_t_text = self.date_time.strftime("%m-%d-%Y %H-%M-%S")
        self.invisible_label = tk.Label()
        self.inv = tk.Label()
        self.invisible_label.after(60000,self.date_time_update)
 
    
    def noti_field(self):
            for d_t in self.object.event_dict:
                for e in self.object.event_dict[d_t]:
                    if isinstance(e,CalenderMeeting) and e.reminder_for_meeting(self.date_time):
                        response = messagebox.askquestion('Upcoming meeting','You have a meeting coming up')
                        if response == 'yes':
                            e.open_link()
                    elif e.notification(self.date_time):
                        self.noti_toast()
                        break

    def noti_toast(self):
        wintoaster = WindowsToaster('Event Update')
        newToast = ToastText1()
        newToast.SetBody('You have one or more upcoming event')
        wintoaster.show_toast(newToast)
    
    def date_time_update(self):
        self.date_time = datetime.datetime.today()
        self.noti_field()
        self.invisible_label.after(60000,self.date_time_update)
        
