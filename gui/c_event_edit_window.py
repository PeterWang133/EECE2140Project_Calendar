import tkinter as tk
from tkinter import messagebox
import datetime
from object.c_event import CalendarEvent
from object.c_task import CalendarTask
from object.c_arrange import CalendarArrangement
from object.c_meeting import CalenderMeeting
from object.c_deadline import CalendarDeadline
from object.c_eventlibrary import EventLibrary
from object.c_time import CalendarTIme
import object.c_calendar as c_calendar

class EditWindow():
    def __init__ (self,parent,e:CalendarEvent,obj:EventLibrary):
        self.parent = parent
        self.event = e
        self.object = obj

        self.info_frame=tk.Frame(master=self.parent)
        self.info_label = tk.Label(master=self.info_frame,text='Original Info')
        self.info_text = tk.Text(master=self.info_frame, height=20, width=35)
        
        self.info_text.insert(tk.END,e.__str__())

        self.info_label.pack(side=tk.TOP)
        self.info_text.pack(side=tk.BOTTOM)
        self.info_frame.pack(side=tk.LEFT)

        self.event_display()
    
    def event_display(self):
        self.date_time = self.event.date_time
        self.event_details = self.event.event_details
        self.reminder = self.event.reminder
        self.reminder_type='none'

        self.d_t_label = tk.Label(master=self.parent, text='Datetime')
        self.d_t_label.pack()
        self.d_t_text = tk.Text(master=self.parent,width=20, height=1)
        self.d_t_text.pack()
        self.d_t_text.insert(tk.END, self.date_time.strftime("%m-%d-%Y %H:%M"))

        self.e_d_label = tk.Label(master=self.parent,text='Event Details')
        self.e_d_label.pack()
        self.e_d_text = tk.Text(master=self.parent, width=20,height=3)
        self.e_d_text.pack()
        self.e_d_text.insert(tk.END,self.event_details)

        self.reminder_type_frame = tk.Frame(master=self.parent)
        self.reminder_type_frame.pack(side=tk.TOP)

        self.reminder_label = tk.Label(master=self.reminder_type_frame,text='Select the reminder time')
        self.reminder_val = ['none','minutes', 'hours', 'days']  
        remind_value = tk.StringVar(value=self.reminder_val)
        self.reminder_box = tk.Listbox(master=self.reminder_type_frame,listvariable=remind_value, width=20, height=5)
        self.reminder_box.select_set(0)
        self.reminder_type_frame.pack(side=tk.TOP)
        self.reminder_label.pack()
        self.reminder_box.pack()

        self.set_reminder_frame = tk.Frame(master=self.parent) 
        self.set_reminder_frame.pack(side=tk.TOP) 

        self.reminder_box.bind('<<ListboxSelect>>', self.reminder_select)

        self.button_frame = tk.Frame(master=self.parent)
        self.button_frame.pack(side=tk.BOTTOM)

        self.save_button = tk.Button(master=self.button_frame,text='Save', command=self.save_edit)
        self.delete_button = tk.Button(master=self.button_frame,text='Delete',command=self.delete_event)
        self.cancel_button = tk.Button(master=self.button_frame, text='Cancel', command=self.cancel_edit)
        self.save_button.pack(side=tk.LEFT)
        self.delete_button.pack(side=tk.LEFT)
        self.cancel_button.pack(side=tk.LEFT)


        if isinstance(self.event, CalendarArrangement):
            self.arrangement_display()
        elif isinstance(self.event,CalenderMeeting):
            self.meeting_display()

    def reminder_select(self,event):
        index = self.reminder_box.curselection()[0]
        self.reminder_type = self.reminder_box.get(index)
        self.set_reminder_frame.pack_forget()
        if self.reminder_type == 'none':
            self.reminder = False
        else:
            self.set_reminder_frame = tk.Frame(master=self.parent,height=2) 
            self.set_reminder_frame.pack(side=tk.TOP) 
            self.set_reminder()
    
    def set_reminder(self):
        self.set_reminder_label = tk.Label(master=self.set_reminder_frame, text='Set Reminder')
        self.set_reminder_text = tk.Text(master=self.set_reminder_frame, width=10, height=1)
        self.set_reminder_label.pack(side=tk.TOP)
        self.set_reminder_text.pack(side=tk.BOTTOM)

    def reminder_setup(self):
        if self.reminder_type!='none':
            value=self.set_reminder_text.get('1.0',tk.END)
            value=value.split()
            value = ''.join(value)
            value = int(value)
            if self.reminder_type == 'minutes':
                self.reminder = datetime.timedelta(minutes=value)
            elif self.reminder_type == 'hours':
                self.reminder = datetime.timedelta(hours=value)
            elif self.reminder_type == 'days':
                self.reminder = datetime.timedelta(days=value)

    def arrangement_display(self):
        self.recurring_frame = tk.Frame(master=self.parent)
        self.recurring_label = tk.Label(master=self.recurring_frame,text='Recurring Type')
        self.recurring_lst = ['None', 'Hourly', 'Daily', 'Weekly', 'Monthly', 'Yearly']
        self.recurring_val = tk.StringVar(value=self.recurring_lst)
        self.recurring_lstbox = tk.Listbox(master=self.recurring_frame,listvariable=self.recurring_val)
        self.recurring_label.pack(side=tk.TOP)
        self.recurring_lstbox.pack(side=tk.BOTTOM)
        self.recurring_frame.pack(side=tk.BOTTOM)

        self.recurring_lstbox.bind('<<ListboxSelect>>', self.recurring_selection)

    def recurring_selection(self, event):
        index = self.recurring_lstbox.curselection()[0]
        self.recurring = self.recurring_lstbox.get(index)
        self.recurring = ''.join(self.recurring.split())

    def meeting_display(self):
        self.link_frame = tk.Frame(master=self.parent)
        self.link_label = tk.Label(master=self.link_frame,text='Link')
        self.link_text = tk.Text(master=self.link_frame,width=30,height=1)

        self.link = self.event.link
        self.link_text.insert(tk.END,self.link)

        self.link_label.pack(side=tk.TOP)
        self.link_text.pack(side=tk.BOTTOM)
        self.link_frame.pack(side=tk.BOTTOM)


    def save_edit(self):
        response = messagebox.askquestion('Save', 'Save changes?')
        if response == 'yes':
            self.date_time = self.d_t_text.get('1.0', tk.END)
            self.date_time = ' '.join(self.date_time.split())
            self.date_time+=':00'
            self.date_time = datetime.datetime.strptime(self.date_time, "%m-%d-%Y %H:%M:%S")

            self.event_details = self.e_d_text.get('1.0', tk.END)
            self.event_details = ' '.join(self.event_details.split())

            self.event.date_time = self.date_time
            self.event.event_details = self.event_details

            self.reminder_setup()
            self.event.reminder = self.reminder

            if isinstance(self.event, CalendarArrangement):
                self.event.recurring = self.recurring
        
            if isinstance(self.event, CalenderMeeting):
                self.link = self.link_text.get('1.0', tk.END)
                self.link = ''.join(self.link.split())
                self.event.link = self.link
        
            print(self.event)

            self.parent.destroy()

    def cancel_edit(self):
        response = messagebox.askquestion('Cancel Edit', 'Are you sure you want to cancel edit?')
        if response=='yes':
            self.parent.destroy()

    def delete_event(self):
        response = messagebox.askquestion('Delete', 'Are you sure to delete the event?')
        if response == 'yes':
            self.object.del_event(self.event.date_time,self.event)
            self.parent.destroy()
