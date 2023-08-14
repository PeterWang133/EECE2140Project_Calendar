import datetime
from object.c_time import CalendarTIme
from abc import abstractclassmethod

import winsound

class CalendarEvent(CalendarTIme):
    def __init__(self, date_time:CalendarTIme, event_details:str, reminder=False) -> None:
        super().__init__(date_time)
        self.event_details = event_details
        self.reminder = reminder
        self.delay_time = ''
    
    def create_delay_time(self, delay_time):
        self.delay_time = self.date_time-self.reminder+delay_time

    def notification(self, current_time:datetime):
        if self.reminder!=False:
            t = self.date_time-self.reminder
            return self.reminder and current_time.date() == t.date() and current_time.strftime("%H:%M") == t.strftime("%H:%M")
            #winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        return False
    
    def delay_noti(self, current_time:datetime):
        if self.reminder and current_time.date() == self.delay_time.date() and current_time.hour == self.delay_time.hour and current_time.minute == self.delay_time.minute:
            return True
        else:
            return False
    
    def modify_event_details(self, new_detail):
        self.event_details = new_detail
    
    def modify_datetime(self, new_datetime):
        self.date_time = new_datetime

    def __str__(self) -> str:
        if self.reminder=='' or self.reminder==False:
            s='off'
        else:
            s=str(self.reminder)+' before the event'
        return f'{super().__str__()}\nReminder: {s}\nEvent Description: {self.event_details}'
    
    @abstractclassmethod
    def write_to_file(self):
        pass
