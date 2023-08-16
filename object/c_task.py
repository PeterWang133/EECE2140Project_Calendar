from object.c_event import CalendarEvent
import datetime

class CalendarTask(CalendarEvent):
    """A CalendarTask class that calls for all task type event which is a subclass of CalendarTask"""
    def __init__(self, date_time: datetime, event_details: str, reminder) -> None:
        """Initializes the CalendarTask object"""
        super().__init__(date_time, event_details, reminder)
        self.reminder = reminder

    def __str__(self) -> str:
        """Prints out the CalendarTask object
        : param self: a CalendarTask object
        : return: a String
        """
        return f'Task\n{super().__str__()}\n'
    
    def write_to_file(self):
        """Writes the CalendarTask into a text file in String format
        : param self: a CaledarTask object
        : return: a String
        """
        r = self.reminder
        if self.reminder != False:
            r = self.date_time-self.reminder
            r = datetime.datetime.strftime(r,'%m-%d-%Y,%H:%M:%S')
        return 'Task '+f'{self.date_time} '+f'{self.event_details} '+f'{r}'
    
            


        
