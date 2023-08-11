from object.c_event import CalendarEvent
import datetime
import webbrowser

class CalenderMeeting(CalendarEvent):
    def __init__(self, date_time: datetime, event_details: str, reminder=datetime.timedelta(minutes=5), link='') -> None:
        super().__init__(date_time, event_details,reminder)
        self.reminder = reminder
        self.link = link

    def open_link (self, current_time:datetime):
        if self.link!='' and self.date_time-self.reminder == current_time:
            webbrowser.open(self.link)
    
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