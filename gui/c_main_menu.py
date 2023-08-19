import tkinter as tk

from object.c_eventlibrary import EventLibrary

from gui.c_greeting import Greeting
from gui.c_calendar_view import TkinterCalendar
from gui.c_search_window import Search
from gui.c_create_event import CreateEvent
from gui.c_event_editor import EventEditor
from gui.c_notification import Notification

class HomeScreen(tk.Frame):
    """A HomeScreen class that which is a subclass of Frame"""

    def __init__(self, parent, obj:EventLibrary) -> None:
        '''initializes a home screen object
        params: self a HomeScreen object, parent, and Event Library Object
        returs: None'''
        super().__init__(parent)
        self.parent = parent
        self.parent.title('Main Menu')
        self.object = obj
        obj.read_file()
        self.home_field()
        self.noti_field()
    
    def home_field(self):
        ''' creates the buttons in the main menu
        params: self- HomeScreen Object
        returns: None'''
        g = Greeting(self.parent, self.object)
        g.pack(side=tk.RIGHT)
        button_frame = tk.Frame(master=self.parent)
        create_button = tk.Button(master=button_frame,text='Create',command=self.create_event)
        edit_button = tk.Button(master=button_frame, text='Edit',command=self.edit_event)
        search_button = tk.Button(master=button_frame, text='Search', command=self.search_event)
        calendar_button = tk.Button(master=button_frame,text='Calendar',command=self.call_calendar)
        calendar_button.pack(side=tk.LEFT)
        create_button.pack(side=tk.LEFT)
        edit_button.pack(side=tk.LEFT)
        search_button.pack(side=tk.LEFT)
        button_frame.pack(side=tk.BOTTOM)

    def create_event(self):
        ''' a function to open a new window and call the CreateEvent function
        params; self- HomeScreen object
        returns: None'''
        new_window = tk.Toplevel()
        new_window.title('Create Event')
        c = CreateEvent(new_window,self.object)
    
    def edit_event(self):
        ''' a function to open a new window and call the EventEditor function
        params: self- HomeScreen object'''
        new_window = tk.Toplevel()
        new_window.title('Event Editor')
        new_window.geometry('690x450')
        new_window.resizable(True,True)
        e = EventEditor(new_window,self.object)
    
    def search_event(self):
        ''' a function to open a new window and call the Search function
        params: self- HomeScreen object'''
        new_window = tk.Toplevel()
        new_window.title('Search Event')
        s = Search(new_window,self.object)
    
    def call_calendar(self):
        '''Open the calendar GUI.'''
        c = TkinterCalendar(self.object)
    
    def noti_field(self):
        """Display the notificaiton field"""
        n = Notification(self.object)

