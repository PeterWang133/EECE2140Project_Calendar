import datetime
from object.c_event import CalendarEvent

class CalendarDeadline(CalendarEvent):
    def __init__(self, date_time: datetime, event_details: str, reminder=datetime.timedelta(days=1)) -> None:
        super().__init__(date_time, event_details,reminder)
        self.reminder = reminder

    def count_down(self, date_time:datetime):
        day = date_time-self.date_time
        return int(day.days)
    
    def __str__(self) -> str:
        current_dt = datetime.datetime.today()
        if current_dt.date()>self.date_time.date():
            return 'Deadline\n'+super().__str__()+'\n'+f'{self.count_down(current_dt)} day(s) has passed.\n'
        elif current_dt.date() == self.date_time.date():
            return 'Deadline\n'+super().__str__()+'\n'+f'Deadline is today.\n'
        elif current_dt<self.date_time:
            return 'Deadline\n'+super().__str__()+'\n'+f'{-1*self.count_down(current_dt)} day(s) left.\n'
        
    def write_to_file(self):
        r = self.reminder
        if self.reminder != False:
            r = self.date_time-self.reminder
            r = datetime.datetime.strftime(r,'%m-%d-%Y,%H:%M:%S')
        s='Deadline '+f'{self.date_time} '+f'{self.event_details} '+f'{r}'
        return s