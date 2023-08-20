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
    ''' Creates the Notification class'''
    def __init__(self,obj:EventLibrary):
        ''' Initialize the notification class
        Args: EventLibrary obj
        Returns: None'''
        self.object = obj
        self.noti_lst = []
        self.date_time = datetime.datetime.today()
        self.d_t_text = self.date_time.strftime("%m-%d-%Y %H-%M-%S")
        self.invisible_label = tk.Label()
        self.inv = tk.Label()
        self.reminded= False
        self.reminded_time=self.date_time
        self.invisible_label.after(5000,self.date_time_update)
 
    
    def noti_field(self):
        ''' Creates the notification field, and also opens links for upcoming meetings '''
        if self.date_time.strftime("%m-%d-%Y %H:%M") != self.reminded_time.strftime("%m-%d-%Y %H:%M"):
            self.reminded=False
            for d_t in self.object.event_dict:
                for e in self.object.event_dict[d_t]:
                    if isinstance(e,CalenderMeeting) and e.reminder_for_meeting(self.date_time):
                        self.reminded_time=self.date_time
                        response = messagebox.askquestion('Upcoming meeting','You have a meeting coming up')
                        if response == 'yes':
                            e.open_link()
                    elif e.notification(self.date_time) and self.reminded==False:
                        self.noti_toast()
                        self.reminded = True
                        self.reminded_time = self.date_time
                        break

    def noti_toast(self):
        ''' diaplays the notification the the users screen via windows default notifications'''
        noti_t = WindowsToaster('Event Update')
        newToast = ToastText1()
        newToast.SetBody('You have one or more upcoming event')
        noti_t.show_toast(newToast)
    
    def date_time_update(self):
        ''' updates the date and time for the notification'''
        self.date_time = datetime.datetime.today()
        self.noti_field()
        self.invisible_label.after(5000,self.date_time_update)
        
