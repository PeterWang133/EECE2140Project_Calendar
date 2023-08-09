import tkinter as tk
from object.c_task import CalendarTask
from object.c_arrange import CalendarArrangement
from object.c_meeting import CalenderMeeting
from object.c_deadline import CalendarDeadline
from object.c_eventlibrary import EventLibrary
from object.c_time import CalendarTIme
import object.c_calendar as c_calendar
from gui.c_event_edit_window import EditWindow
 
class EventEditor():
    def __init__(self, parent, object:EventLibrary) -> None:
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

        self.date_type_box.bind('<<ListboxSelect>>', self.date_box_select)
        self.event_type_box.bind('<<ListboxSelect>>', self.event_type_field)
        self.search_button = tk.Button(master=self.search_frame, text='Search', command=self.search_command)
        self.search_button.pack()

        self.result_frame = tk.Frame(master=self.parent)
        self.result_frame.pack(side=tk.RIGHT)
        self.result_lstbox = tk.Listbox(master=self.result_frame)

    def date_box_select(self,event):
        selected_index = self.date_type_box.curselection()[0]
        self.date_type_selection = self.date_type_box.get(selected_index)
        if self.date_type_selection == 'Date':
            self.search_single_date()
        elif self.date_type_selection == 'Date Range':
            self.search_date_range()
    
    def search_date_field(self):
        self.date_frame = tk.Frame(master=self.parent,relief='groove', borderwidth=5)
        self.date_frame.pack(side=tk.LEFT)

    def search_single_date(self):
        self.date_frame.pack_forget()
        self.date_frame = tk.Frame(master=self.parent,relief='groove', borderwidth=5)
        self.date_label = tk.Label(master=self.date_frame)
        self.date_search = tk.Text(master=self.date_frame,height=1, width=15)
        self.date_label['text'] = 'Enter the date'
        self.date_label.pack()
        self.date_search.pack()
        self.date_frame.pack(side=tk.LEFT)

    def search_date_range(self):
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
        selected_event = self.event_type_box.curselection()[0]
        self.event_type_selection = self.event_obj_lst[selected_event]
    
    def key_word_field(self):
        self.key_word_text = tk.Text(master=self.search_frame, width=20, height=2)
        self.key_word_text.pack()
    
    def search_command(self):
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
        self.result_lstbox.pack()
        self.result_field()

    def result_field(self):
        self.obj_lst = []
        i=0
        self.result_lstbox.delete(0,tk.END)
        for d_t in self.search_result_obj:
            for e in self.search_result_obj[d_t]:
                self.obj_lst.append(e)
                self.result_lstbox.insert(i,e)
                i += 1
        
        self.result_lstbox.bind('<<ListboxSelect>>',self.selected_event)
    
    def selected_event(self,event):
        index = self.result_lstbox.curselection()[0]
        self.selected_choice = self.obj_lst[index]
        self.edit_field()
    
    def edit_field(self):
        new_window = tk.Toplevel()
        edit_window = EditWindow(new_window,self.selected_choice, self.object)
        

        
