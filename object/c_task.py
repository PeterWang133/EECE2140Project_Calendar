from object.c_event import CalendarEvent
import datetime

class CalendarTask(CalendarEvent):
    def __init__(self, date_time: datetime, event_details: str, reminder) -> None:
        super().__init__(date_time, event_details, reminder)
        self.reminder = reminder

    def __str__(self) -> str:
        return f'Task\n{super().__str__()}\n'
    
    def write_to_file(self):
        r = self.reminder
        if self.reminder != False:
            r = self.date_time-self.reminder
            r = datetime.datetime.strftime(r,'%m-%d-%Y,%H:%M:%S')
        return 'Task '+f'{self.date_time} '+f'{self.event_details} '+f'{r}'
    
            


        
