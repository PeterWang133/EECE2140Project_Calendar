import datetime
import tkinter as tk
from object.c_eventlibrary import EventLibrary
import object.c_calendar as c_calendar
import calendar
import functools

class CalendarView(calendar.Calendar):
    ''' CalendarView class which is a subclass of Calendar'''

    def __init__(self, obj:EventLibrary, firstweekday: int = 0) -> None:
        '''Create the calendar display frame within the GUI.
    Args:
        self: The TkinterCalendar object
        parent: The parent Tkinter window where the calendar will be displayed
        year: The year of the calendar to display
        month: The month (1-12) of the calendar to display

    Returns:
        None '''
        super().__init__(firstweekday)
        new_window = tk.Toplevel()
        new_window.title('Calendar View')
        self.current_time = datetime.datetime.today()
        self.year = self.current_time.year
        self.month = self.current_time.month
        self.parent = new_window
        self.obj = obj
        self.frame = tk.Frame(master=new_window)
        self.event_text=tk.Text(master=new_window)
        self.calendar_frame(new_window,self.year,self.month)
        self.button_frame = tk.Frame(master=new_window,relief='groove', borderwidth=5)
        self.previous_button = tk.Button(master=self.button_frame,text="Previous", command=self.previous_month)
        self.next_button = tk.Button(master=self.button_frame,text='Next',command=self.next_month)
        self.event_text.pack(side=tk.TOP)
        self.previous_button.pack(side=tk.LEFT)
        self.next_button.pack(side=tk.RIGHT)
        self.button_frame.pack(side=tk.TOP)
        self.frame.pack(side=tk.BOTTOM)
        self.label.pack(side=tk.BOTTOM)

    def formatmonth(self, parent, year, month):
        '''Format and display a month in the calendar GUI
    Args:
        self (TkinterCalendar): The TkinterCalendar object
        parent (tk.Tk): The parent Tkinter window where the month will be displayed
        year (int): The year of the month to display
        month (int): The month (1-12) to display
    Returns:
        tk.Frame: A properly sized month display with buttons for each day in the month'''

        dates = self.monthdatescalendar(year, month)

        frame = tk.Frame(parent)

        self.labels = []

        for r, week in enumerate(dates):
            labels_row = []
            for c, date in enumerate(week):
                label = tk.Button(frame, text=date.strftime('%Y\n%m\n%d'))
                label['command'] = functools.partial(self.button_click, label['text'])
                label.grid(row=r, column=c)
                if date.month != month:
                    label['bg'] = '#aaa'
                if c == 6:
                    label['fg'] = 'red'
                labels_row.append(label)
            self.labels.append(labels_row)
        return frame
    
    def calendar_frame (self, parent, year, month):
        '''Create the calendar display frame within the GUI
    params:
        self: TkinterCalendar object
        parent (tk.Tk): The parent Tkinter window where the calendar will be displayed
        year (int): The year of the calendar to display
        month (int): The month (1-12) of the calendar to display
    Returns: None'''
        self.frame = self.formatmonth(parent, year, month)
        self.frame.pack(side=tk.BOTTOM)
        self.label = tk.Label(parent, text = '{} / {}'.format(year, month))
        self.label.pack(side=tk.BOTTOM)
        
        
    def previous_month(self):
        ''' function to update the calendar when previsou month is clicked
        params:
             self: Tkinter Calendar object
         Returns: None '''
        self.label.destroy()
        self.frame.destroy()
        self.month = self.month-1
        if self.month == 0:
            self.month = 12
            self.year -= 1
        self.calendar_frame(self.parent,self.year,self.month)

    def next_month(self):
        ''' function to update the calendar when previsou month is clicked
        params: self- Tkinter Calendar object
         Returns: None '''
        self.label.destroy()
        self.frame.destroy()
        self.month = self.month+1
        if self.month == 13:
            self.month = 1
            self.year += 1
        self.calendar_frame(self.parent,self.year,self.month)
        

    def button_click(self,date_time):
        ''' function to handle button presses on the GUI
        params: Self- HomeScreen object
        date_time- datetime object'''
        self.event_text.configure(state='normal')
        self.event_text.delete('1.0',tk.END)
        date_time = date_time.split('\n')
        date_time = [date_time[1], date_time[2], date_time[0]]
        date_time = '-'.join(date_time)
        s=c_calendar.search_and_sort(self.obj,[date_time, date_time],'','',False)
        self.event_text.insert(tk.END,s)
        self.event_text.configure(state='disabled')
        

        
    
    
