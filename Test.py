import datetime
import tkinter as tk
from tkinter import messagebox
from object.c_eventlibrary import EventLibrary
from object.c_task import CalendarTask
from object.c_deadline import CalendarDeadline
from object.c_arrange import CalendarArrangement
from object.c_meeting import CalenderMeeting
from gui.c_main_menu import HomeScreen
from gui.c_notification import Notification
from object.c_event import CalendarEvent

import webbrowser

events = EventLibrary()

root = tk.Tk()
h = HomeScreen(root,events)

root.mainloop()
