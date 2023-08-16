import datetime

class CalendarTIme:
    """A CalendarTIme class that manages the date and time"""
    def __init__(self, date_time:datetime) -> None:
        """Initializes a CalndarTIme object"""
        self.date_time = date_time

    def weekday_lst(self):
        """Converts the date into a weekday
        : param self: a CalendarTIme object
        : return: a String
        """
        wd = self.date_time.weekday()
        weekday_lst = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return weekday_lst[wd]
    
    def month_lst(self):
        """Converts the month into a String
        : param self: a CalendarTIme object
        : return: a String
        """
        m = self.date_time.month
        month_lst = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','September', 'October', 'November', 'Deceber']
        return month_lst[m-1]

    def __str__(self) -> str:
        """Prints out the date and time
        : param self: a CalendarTIme object
        : return: a String
        """
        return f'Date and Time: {self.date_time.strftime("%m-%d-%Y %H:%M")}'