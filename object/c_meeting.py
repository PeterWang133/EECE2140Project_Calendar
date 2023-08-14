from object.c_event import CalendarEvent
import datetime
import webbrowser

class CalenderMeeting(CalendarEvent):
    def __init__(self, date_time: datetime, event_details: str, reminder=datetime.timedelta(minutes=5), link='') -> None:
        super().__init__(date_time, event_details,reminder)
        self.reminder = reminder
        self.link = link

    def open_link (self):
            webbrowser.open(self.link)
    
    def reminder_for_meeting(self,current_time:datetime):
        reserve_time = self.date_time-datetime.timedelta(minutes=5)
        return self.reminder!=False and self.link!='' and current_time.strftime("%m-%d-%Y %H:%M") == reserve_time.strftime("%m-%d-%Y %H:%M")
    
    def __str__(self) -> str:
        s=''
        if self.link!='':
            s='\nLink: '+self.link
        return 'Meeting\n'+super().__str__()+f'{s}\n'
    
    def write_to_file(self):
        r = self.reminder
        if self.reminder != False:
            r = self.date_time-self.reminder
            r = datetime.datetime.strftime(r,'%m-%d-%Y,%H:%M:%S')
        l = 'empty'
        if self.link!='':
            l = self.link
        return 'Meeting '+f'{self.date_time} '+f'{self.event_details} '+f'{r} '+f'{l}'