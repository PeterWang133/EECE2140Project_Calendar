import datetime

class CalendarTIme:
    def __init__(self, date_time:datetime) -> None:
        self.date_time = date_time

    def weekday_lst(self):
        wd = self.date_time.weekday()
        weekday_lst = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return weekday_lst[wd]
    
    def month_lst(self):
        m = self.date_time.month
        month_lst = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','September', 'October', 'November', 'Deceber']
        return month_lst[m-1]
    
    def ttt (self):
        return self.date_time.time.strftime("%I:%M %p")

    def __str__(self) -> str:
        return f'Date and Time: {self.date_time.strftime("%m-%d-%Y %H:%M")}'