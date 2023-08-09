import tkinter as tk
from tkinter import messagebox
import webbrowser
import winsound

from object.c_eventlibrary import EventLibrary
from object.c_event import CalendarEvent
from object.c_meeting import CalenderMeeting

class Notification(tk.Frame):
    def __init__(self,parent,object:EventLibrary):
        super().__init__(parent)
        self.parent = parent
        self.object = object
    
    def noti_field(self):
        response = messagebox.askquestion('Upcoming Event', 'You have an upcoming event')
    
    def reminder_lst(self):
        reminder_lst = []
        for d_t in self.object.event_dict:
            for e in self.object.event_dict[d_t]:
                if e.reminder != False:
                    reminder_lst.append(e)

