import tkinter as tk
from object.c_task import CalendarTask
from object.c_arrange import CalendarArrangement
from object.c_meeting import CalenderMeeting
from object.c_deadline import CalendarDeadline
from object.c_eventlibrary import EventLibrary
import object.c_calendar as c_calendar

class Search(tk.Frame):
    ''' class for displaying the search field in the GUI'''
    def __init__(self, parent, object:EventLibrary) -> None:
        '''Initializes the Search class.
        Args:
            parent: The parent widget where the search interface will be placed
            object: An EventLibrary object
        '''
        super().__init__(parent)
        self.parent = parent
        self.object = object
        self.search_field()
    

    def search_field(self):
        '''Creates the search field GUI elements.'''
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

        self.alpha_label = tk.Label(master=self.search_frame, text='Sort by Alphabets')
        self.alpha_label.pack()
        self.alphabet_field()

        self.date_type_box.bind('<<ListboxSelect>>', self.date_box_select)
        self.event_type_box.bind('<<ListboxSelect>>', self.event_type_field)
        self.search_button = tk.Button(master=self.search_frame, text='Search', command=self.search_command)
        self.search_button.pack()

        self.result_frame = tk.Frame(self.parent)
        self.result_frame.pack(side=tk.RIGHT)
        self.result_text = tk.Text(master=self.result_frame)

    def date_box_select(self,event):
        '''Handles the user's selection of the date type (single date or date range).'''
        selected_index = self.date_type_box.curselection()
        if selected_index:
            selected_index=selected_index[0]
            self.date_type_selection = self.date_type_box.get(selected_index)
            if self.date_type_selection == 'Date':
                self.search_single_date()
            elif self.date_type_selection == 'Date Range':
                self.search_date_range()
    
    def search_date_field(self):
        '''Creates the frame for date-related search options.'''
        self.date_frame = tk.Frame(master=self.parent,relief='groove', borderwidth=5)
        self.date_frame.pack(side=tk.LEFT)

    def search_single_date(self):
        '''Creates the GUI elements for searching a specific date.'''
        self.date_frame.pack_forget()
        self.date_frame = tk.Frame(master=self.parent,relief='groove', borderwidth=5)
        self.date_label = tk.Label(master=self.date_frame)
        self.date_search = tk.Text(master=self.date_frame,height=1, width=15)
        self.date_label['text'] = 'Enter the date'
        self.date_label.pack()
        self.date_search.pack()
        self.date_frame.pack(side=tk.LEFT)

    def search_date_range(self):
        '''Creates the GUI elements for searching within a date range.'''
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
        '''Handles the user's selection of the event type.'''
        selected_event = self.event_type_box.curselection()
        if selected_event:
            selected_event=selected_event[0]
            self.event_type_selection = self.event_obj_lst[selected_event]
    
    def key_word_field(self):
        '''Creates the text box for entering search keywords.'''
        self.key_word_text = tk.Text(master=self.search_frame, width=20, height=2)
        self.key_word_text.pack()

    def alphabet_field(self):
        '''Creates the listbox for selecting alphabetical sorting.'''
        self.alpha_lst = ['Yes','No']
        alpha_val = tk.StringVar(value=self.alpha_lst)
        self.alpha_lstbox = tk.Listbox(master=self.search_frame,width=10, height=2, listvariable=alpha_val)
        self.alpha_lstbox.pack()
        self.alpha_lstbox.bind('<<ListboxSelect>>', self.alphabet_on_off)

    def alphabet_on_off(self,event):
        '''Handles the user's selection of alphabetical sorting.'''
        index = self.alpha_lstbox.curselection()
        if index:
            index=index[0]
            selected_choice = self.alpha_lstbox.get(index)
            if selected_choice == 'Yes':
                self.alphabet = True
            else:
                self.alphabet = False
    
    def search_command(self):
        '''Executes the search and sort operation based on user inputs.'''
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
        self.search_result = c_calendar.search_and_sort(self.object,self.date_lst,self.event_type_selection,self.key_word,self.alphabet)
        self.result_text.pack()
        self.result_field()

    def result_field(self):
        '''Displays the search results in the text box.'''
        self.result_text.configure(state='normal')
        self.result_text.delete('1.0', tk.END)
        self.result_text.insert(tk.END, self.search_result)
        self.result_text.configure(state='disable')






            
        
            


