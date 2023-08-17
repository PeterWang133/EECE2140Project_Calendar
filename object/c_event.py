import datetime
from object.c_time import CalendarTIme
from abc import abstractclassmethod

#import winsound

class CalendarEvent(CalendarTIme):
    """A CalendarEvent class that calls for all types of events which is a subclass of CalendarTIme"""
    def __init__(self, date_time:CalendarTIme, event_details:str, reminder=False) -> None:
        """Initializes a CalendarEvent object"""
        super().__init__(date_time)
        self.event_details = event_details
        self.reminder = reminder

    def notification(self, current_time:datetime):
        """Checks if the current time matches the time set up by the user for sending the notification
        : param self: a CalendarEvent object, current_time: a datetime object
        : return: Boolean
        """
        if self.reminder!=False:
            t = self.date_time-self.reminder
            return self.reminder and current_time.date() == t.date() and current_time.strftime("%H:%M") == t.strftime("%H:%M")
            #winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        return False
    
    def modify_event_details(self, new_detail):
        """Modifies the event detail of the current CalendarEvent with the new event details
         :param self: a CalendarEvent object, new_detail: a String
         :return: new event details
        """
        self.event_details = new_detail
    
    def modify_datetime(self, new_datetime):
        """Modifies the date and time of the current CalendarEvent with new date and time
         :param self: a CalendarEvent object, new_datetime: a datetime object
         :return: new date and time
        """
        self.date_time = new_datetime

    def __str__(self) -> str:
        """Prints out the date and time, event details, and reminder time
        : param self: a CalendarEvent object
        : return: a String
        """
        if self.reminder=='' or self.reminder==False:
            s='off'
        else:
            s=str(self.reminder)+' before the event'
        return f'{super().__str__()}\nReminder: {s}\nEvent Description: {self.event_details}'
    
    @abstractclassmethod
    def write_to_file(self):
        pass
