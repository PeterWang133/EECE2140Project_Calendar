import tkinter as tk
import datetime
from object.c_task import CalendarTask
from object.c_arrange import CalendarArrangement
from object.c_meeting import CalenderMeeting
from object.c_deadline import CalendarDeadline
from object.c_eventlibrary import EventLibrary

class CreateEvent():
    def __init__(self,parent,obj:EventLibrary):
        self.parent = parent
        self.object = obj
        self.create_event_window()

    def create_event_window(self):
        self.win_frame = tk.Frame(master=self.parent)
        self.type_label = tk.Label(master=self.win_frame, text='Select a Type')
        self.type_label.pack()

        self.type_list = ['Task', 'Arrangement', 'Meeting', 'Deadline']
        self.type_obj_lst = [CalendarTask, CalendarArrangement, CalenderMeeting, CalendarDeadline]
        self.type_value = tk.StringVar(value=self.type_list)
        self.type_lstbox = tk.Listbox(master=self.win_frame, listvariable=self.type_value, width=20, height=5)
        self.type_lstbox.pack()

        self.event_frame = tk.Frame(master=self.parent)
        self.event_frame.pack(side=tk.RIGHT)

        self.d_t_label = tk.Label(master=self.win_frame,text='Date')
        self.win_frame.pack(side=tk.TOP)
        self.date_box = tk.Text(master=self.win_frame,width=10,height=1)

        self.d_t_label_2 = tk.Label(master=self.win_frame,text='Time')
        self.time_box = tk.Text(master=self.win_frame,width=10,height=1)

        self.e_d_label = tk.Label(master=self.win_frame, text='Event Details')
        self.detail_text=  tk.Text(master=self.win_frame, width=15, height=6)
        
        self.r_label = tk.Label(master=self.win_frame, text='Reminder Type')
        self.reminder_type_lst = ['on', 'off']
        self.reminder_value = tk.StringVar(value=self.reminder_type_lst)
        self.reminder_type_lstbox = tk.Listbox(master=self.win_frame,listvariable=self.reminder_value, width=20, height=2)

        self.reminder_type_frame = tk.Frame(master=self.parent)
        self.reminder_type_frame.pack(side=tk.BOTTOM)

        self.set_reminder_frame = tk.Frame(master=self.parent)
        self.set_reminder_frame.pack(side=tk.BOTTOM)

        self.function_area()

        self.type_lstbox.bind('<<ListboxSelect>>', self.create_event)
        self.reminder_type_lstbox.bind('<<ListboxSelect>>', self.reminder_option)
    
    def create_event(self,event):
        selected_index = self.type_lstbox.curselection()[0]
        self.event_obj = self.type_obj_lst[selected_index]
        selected_type = self.type_lstbox.get(selected_index)
        self.d_t_label.pack()
        self.date_box.pack()
        self.d_t_label_2.pack()
        self.time_box.pack()
        self.e_d_label.pack()
        self.detail_text.pack()
        self.r_label.pack()
        self.reminder_type_lstbox.pack()

        self.event_frame.pack_forget()
        self.event_frame = tk.Frame(master=self.parent)
        self.event_frame.pack(side=tk.RIGHT)

        if selected_type == 'Task':
            pass
        elif selected_type == 'Arrangement':
            self.arrangement_frame()
        elif selected_type == 'Meeting':
            self.meeting_frame()
        elif selected_type == 'Deadline':
            pass
    
    def arrangement_frame(self):
        self.recurring_label = tk.Label(master=self.event_frame,text='Recurring Type')
        self.recurring_lst = ['None', 'Hourly', 'Daily', 'Weekly', 'Monthly', 'Yearly']
        self.recurring_val = tk.StringVar(value=self.recurring_lst)
        self.recurring_lstbox = tk.Listbox(master=self.event_frame,listvariable=self.recurring_val)
        self.recurring_label.pack()
        self.recurring_lstbox.pack()
        self.recurring_lstbox.bind('<<ListboxSelect>>', self.arrangement_recur)
    
    def arrangement_recur(self,event):
        index = self.recurring_lstbox.curselection()[0]
        self.recurring_selection = self.recurring_lstbox.get(index)

    def meeting_frame(self):
        self.link_label = tk.Label(master=self.event_frame,text='Link')
        self.link_text = tk.Text(master=self.event_frame,width=30,height=1)
        self.link_label.pack()
        self.link_text.pack()
 
    def reminder_option(self,event):
        selected_index = self.reminder_type_lstbox.curselection()[0]
        self.remind_selected_type = self.reminder_type_lstbox.get(selected_index)
        if self.remind_selected_type == 'off':
            self.reminder_frame_off()
        elif self.remind_selected_type == 'on':
            self.reminder_frame_off()
            self.set_reminder_frame.pack_forget()
            self.reminder_frame_on()

    def reminder_frame_off(self):
        self.reminder_type_frame.pack_forget()
        self.set_reminder_frame.pack_forget()
        self.reminder = ''

    def reminder_frame_on(self):
        self.reminder_type_frame = tk.Frame(master=self.parent)
        self.reminder_label = tk.Label(master=self.reminder_type_frame,text='Select the reminder time')
        self.reminder_val = ['minutes', 'hours', 'days']  
        remind_value = tk.StringVar(value=self.reminder_val)
        self.reminder_box = tk.Listbox(master=self.reminder_type_frame,listvariable=remind_value, width=20, height=3)   
        self.reminder_label.pack()
        self.reminder_box.pack()
        self.set_reminder_frame = tk.Frame(master=self.parent)
        self.set_reminder_frame.pack(side=tk.BOTTOM)
        self.reminder_type_frame.pack(side=tk.BOTTOM)
        self.set_reminder_label = tk.Label(master=self.set_reminder_frame, text='Set time')
        self.set_reminder_text = tk.Text(master=self.set_reminder_frame,width=15,height=2)

        self.reminder_box.bind('<<ListboxSelect>>', self.set_reminder)

    def set_reminder(self,event):
        reminder_box_value = self.reminder_box.curselection()[0]
        self.reminder_box_option = self.reminder_box.get(reminder_box_value)
        self.set_reminder_label.pack()
        self.set_reminder_text.pack()
    
    def reminder_setup(self):
        if self.remind_selected_type == 'on':
            value=self.set_reminder_text.get('1.0',tk.END)
            value=value.rstrip()
            value = int(value)
            if self.reminder_box_option == 'minutes':
                self.reminder = datetime.timedelta(minutes=value)
            elif self.reminder_box_option == 'hours':
                self.reminder = datetime.timedelta(hours=value)
            elif self.reminder_box_option == 'days':
                self.reminder = datetime.timedelta(days=value)

    def function_area(self):
        self.function_frame = tk.Frame(master=self.parent)
        self.create_button = tk.Button(master=self.function_frame,text='Create', command=self.create_object)
        self.cancel_button = tk.Button(master=self.function_frame,text='Cancel',command=self.cancel_create)
        self.create_button.pack(side=tk.LEFT)
        self.cancel_button.pack(side=tk.RIGHT)
        self.function_frame.pack(side=tk.BOTTOM)
    
    # Create Object
    def create_object(self):
        self.date = self.date_box.get('1.0', tk.END)
        self.time = self.time_box.get('1.0', tk.END)

        self.date = self.date.rstrip()

        self.time = self.time.rstrip()

        self.string_dt = self.date+' '+self.time+':00'
        self.date_time = datetime.datetime.strptime(self.string_dt, "%m-%d-%Y %H:%M:%S")

        self.event_details = self.detail_text.get('1.0', tk.END)
        self.reminder_setup()
        e=''
        if self.event_obj == CalendarArrangement:
            e=self.event_obj(self.date_time, self.event_details,self.reminder,self.recurring_selection)
            self.object.add_event(e.date_time,e)
        elif self.event_obj == CalenderMeeting:
            link = self.link_text.get('1.0', tk.END)
            link = link.rstrip()
            e=self.event_obj(self.date_time,self.event_details,self.reminder,link)
            self.object.add_event(e.date_time,e)
        else:
            e=self.event_obj(self.date_time,self.event_details,self.reminder)
            self.object.add_event(e.date_time,e)
        self.parent.destroy()
    def cancel_create(self):
        self.parent.destroy()

