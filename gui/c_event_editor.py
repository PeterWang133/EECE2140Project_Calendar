import tkinter as tk
from tkinter import ttk
from object.c_task import CalendarTask
from object.c_arrange import CalendarArrangement
from object.c_meeting import CalenderMeeting
from object.c_deadline import CalendarDeadline
from object.c_eventlibrary import EventLibrary
from object.c_time import CalendarTIme
import object.c_calendar as c_calendar
from gui.c_event_edit_window import EditWindow
import functools
 
class EventEditor():
    '''Class for managing the event editing interface.'''
    def __init__(self, parent, object:EventLibrary) -> None:
        '''Initialize the EventEditor class.
        Args:
            parent (tk.Tk): The parent Tkinter window.
            obj (EventLibrary): The EventLibrary object to manage events.'''
        self.parent = parent
        self.object = object
        self.search_field()

    def search_field(self):
        self.search_frame = tk.Frame(master=self.parent,relief='groove', borderwidth=5)
        self.date_type = tk.Label(master=self.search_frame, text='Search date type')
        self.date_type.pack()
        self.date_type = ['Date', 'Date Range']
        self.d_type = tk.StringVar(value=self.date_type)
        self.date_type_box = tk.Listbox(master=self.search_frame,listvariable=self.d_type, width=20, height=3)
        self.date_type_box.pack()
        self.search_frame.pack(side=tk.LEFT)
        self.search_date_field()

        self.type_label = tk.Label(master=self.search_frame, text='Event Type')
        self.type_label.pack()
        self.event_type_lst = ['All', 'Task', 'Arrangement', 'Meeting', 'Deadline']
        self.event_obj_lst = ['', CalendarTask, CalendarArrangement, CalenderMeeting, CalendarDeadline]
        self.e_type = tk.StringVar(value=self.event_type_lst)
        self.event_type_box = tk.Listbox(master=self.search_frame,listvariable=self.e_type, width=20, height=5)
        self.event_type_box.pack()

        self.key_label = tk.Label(master=self.search_frame, text='Keyword')
        self.key_label.pack()
        self.key_word_field()

        self.result_canvas = tk.Canvas(master=self.parent)
        self.result_frame = tk.Frame(master=self.result_canvas)
        self.scroll_bar = tk.Scrollbar(master=self.parent,orient='vertical')
        self.result_canvas.create_window((0,0),anchor='nw',window=self.result_frame)


        self.date_type_box.bind('<<ListboxSelect>>', self.date_box_select)
        self.event_type_box.bind('<<ListboxSelect>>', self.event_type_field)
        self.search_button = tk.Button(master=self.search_frame, text='Search', command=self.search_command)
        self.search_button.pack()

        self.scroll_bar.configure(command=self.result_canvas.yview)
        self.result_canvas.configure(yscrollcommand=self.scroll_bar.set)

    def date_box_select(self,event):
        '''Handle the selection of date search type.'''
        selected_index = self.date_type_box.curselection()
        if selected_index:
            selected_index = selected_index[0]
            self.date_type_selection = self.date_type_box.get(selected_index)
            if self.date_type_selection == 'Date':
                self.search_single_date()
            elif self.date_type_selection == 'Date Range':
                self.search_date_range()
    
    def search_date_field(self):
        '''Display the date search fields.'''
        self.date_frame = tk.Frame(master=self.parent,relief='groove', borderwidth=5)
        self.date_frame.pack(side=tk.LEFT)

    def search_single_date(self):
        '''Display the search fields for a single date.'''
        self.date_frame.pack_forget()
        self.date_frame = tk.Frame(master=self.parent,relief='groove', borderwidth=5)
        self.date_label = tk.Label(master=self.date_frame)
        self.date_search = tk.Text(master=self.date_frame,height=1, width=15)
        self.date_label['text'] = 'Enter the date'
        self.date_label.pack()
        self.date_search.pack()
        self.date_frame.pack(side=tk.LEFT)

    def search_date_range(self):
        '''Display the search fields for a date range.'''
        self.date_frame.pack_forget()

        self.date_frame = tk.Frame(master=self.parent,relief='groove', borderwidth=5)
        self.start_date_label = tk.Label(self.date_frame)
        self.start_date_label['text'] = 'Enter the start date'
        self.start_date_search = tk.Text(master=self.date_frame,height=1, width=15)

        self.end_date_label = tk.Label(self.date_frame)
        self.end_date_label['text'] = 'Enter the end date'
        self.end_date_search = tk.Text(master=self.date_frame,height=1, width=15)

        self.start_date_label.pack()
        self.start_date_search.pack()
        self.end_date_label.pack()
        self.end_date_search.pack()
        self.date_frame.pack(side=tk.LEFT)
    

    def event_type_field(self,event):
        '''Handle the selection of event type.'''
        selected_event = self.event_type_box.curselection()
        if len(selected_event) != 0:
            selected_event = selected_event[0]
            self.event_type_selection = self.event_obj_lst[selected_event]
    
    def key_word_field(self):
        '''Display the keyword search field.'''
        self.key_word_text = tk.Text(master=self.search_frame, width=20, height=2)
        self.key_word_text.pack()
    
    def search_command(self):
        '''Execute the search command.'''
        self.result_frame.destroy()

        def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
            self.result_canvas.configure(scrollregion=self.result_canvas.bbox('all'))
        
        def on_mousewheel(event):
            if self.scroll_bar.get() != (0.0, 1.0):
                self.result_canvas.yview_scroll(-1 * int(event.delta / 120), "units")
        
        self.result_frame.bind_all("<MouseWheel>", on_mousewheel)
        self.result_frame.bind_all('<Shift-Button-4>', lambda *args: self.result_canvas.yview(tk.SCROLL, -1, tk.UNITS))
        self.result_frame.bind_all('<Shift-Button-5>', lambda *args: self.result_canvas.yview(tk.SCROLL, 1, tk.UNITS))

        if self.date_type_selection=='Date':
            self.date_s = self.date_search.get('1.0', tk.END)
            self.date_lst=self.date_s.split()
        elif self.date_type_selection=='Date Range':
            self.start_d = self.start_date_search.get('1.0', tk.END)
            self.date_lst = self.start_d.split()
            self.end_d = self.end_date_search.get('1.0', tk.END)
            self.date_lst.extend(self.end_d.split())
        self.key_word = self.key_word_text.get('1.0', tk.END)
        self.key_word=self.key_word.split()
        if self.key_word==[]:
            self.key_word=''
        else:
            self.key_word = ' '.join(self.key_word)
        self.search_result_obj = c_calendar.search_and_sort_obj(self.object,self.date_lst,self.event_type_selection,self.key_word)

        self.scroll_bar.pack(side=tk.RIGHT,fill='y')
        self.result_canvas.pack(side=tk.RIGHT)

        self.result_frame = self.result_frame_obj(self.result_canvas)
        self.result_canvas.bind('<Configure>', on_configure)
        self.result_canvas.create_window((0,0),anchor='nw',window=self.result_frame)




    def result_frame_obj(self,parent):
        '''Create the result frame object.'''
        i=0
        frame = tk.Frame(parent)
        for d_t in self.search_result_obj:
            for e in self.search_result_obj[d_t]:
                result_button = tk.Button(master=frame, text=e,width=30,height=6)
                result_button.grid(row=i)
                result_button['command'] = functools.partial(self.edit_field,e)
                i += 1
        return frame

    
    def edit_field(self,event):
        '''Open the event editing window.'''
        new_window = tk.Toplevel()
        new_window.title('Event editor window')
        edit_window = EditWindow(new_window,event, self.object)
        

        
