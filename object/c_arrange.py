import datetime
from object.c_event import CalendarEvent
from object.c_time import CalendarTIme


class CalendarArrangement(CalendarEvent):
    """A CalendarArrangement class that calls for all arrangement type event which is a subclass of CalendarTask"""
    def __init__(self, date_time: CalendarTIme, event_details: str,reminder, recurring: str) -> None:
        """Initializes a CalendarArrangement object"""
        super().__init__(date_time, event_details, reminder)
        self.date_time = date_time
        self.reminder = reminder
        self.recurring = recurring
    
    def remind_hourly(self, date_time):
        """Checks with the current date and time for an arrangement that recurs hourly
        : param self: a CalendarArrangement Object, date_time: a datetime object
        return: a Boolean
        """
        return self.date_time.minute == date_time.minute
    
    def remind_daily(self, date_time):
        """Checks with the current date and time for an arrangement that recurs daily
        : param self: a CalendarArrangement Object, date_time: a datetime object
        return: a Boolean
        """
        return self.date_time.hour == date_time.hour
    
    def remind_weekly(self,date_time:CalendarTIme):
        """Checks with the current date and time for an arrangement that recurs weekly
        : param self: a CalendarArrangement Object, date_time: a datetime object
        return: a Boolean
        """
        d_1 = CalendarTIme(self.date_time)
        d_2 = CalendarTIme(date_time)
        return d_1.weekday_lst() == d_2.weekday_lst()
    
    def remind_monthly(self, date_time):
        """Checks with the current date and time for an arrangement that recurs monthly
        : param self: a CalendarArrangement Object, date_time: a datetime object
        return: a Boolean
        """
        return self.date_time.day == date_time.day
    
    def remind_yearly(self, date_time):
        """Checks with the current date and time for an arrangement that recurs yearly
        : param self: a CalendarArrangement Object, date_time: a datetime object
        return: a Boolean
        """
        return self.date_time.day == date_time.day and self.date_time.month == date_time.month
        
    def remind_event(self, date_time):
        """Checks the recurring type of the CalendarArrangement and determines which method should be used
        for checking time
        : param self: a CalendarArrangement Object, date_time: a datetime object
        return: a Boolean, True if the object recurs and False if the recurring type is 'None'
        """
        arrange = ''
        if self.recurring == 'Yearly':
            arrange=self.remind_yearly(date_time)
        elif self.recurring == 'Monthly':
            arrange=self.remind_monthly(date_time)
        elif self.recurring == 'Weekly':
            arrange=self.remind_weekly(date_time)
        elif self.recurring == 'Daily':
            arrange=self.remind_daily(date_time)
        elif self.recurring == 'Hourly':
            arrange=self.remind_hourly(date_time)
        elif self.recurring == 'None':
            return False
        return arrange
    
    def change_time(self, current_time):
        """Computes the next date and time which the object would appear
        : param self: a CalendarArrangement Object, current_time: a datetime object
        : return: a datetime object
        """
        new_time=0
        if self.recurring == 'Yearly':
            new_time = datetime.datetime(year=current_time.year+1, month=self.date_time.month, day=self.date_time.day, minute=self.date_time.minute, second=self.date_time.second)
        elif self.recurring == 'Monthly':
            new_time = datetime.datetime(year=self.date_time.year, month=current_time.month+1, day=self.date_time.day, minute=self.date_time.minute, second=self.date_time.second)
        elif self.recurring == 'Weekly':
            new_time = current_time + datetime.timedelta(days=7)
        elif self.recurring == 'Daily':
            new_time = current_time + datetime.timedelta(days=1)
        elif self.recurring == 'Hourly':
            new_time = current_time + datetime.timedelta(hours=1)
        return new_time
    
    def check_recur(self,start,end):
        """Checks if an object should appear in a time range
        : param self: a CalendarArrangement, start: a datetime object, end: a datetime object
        : return: True if the object does recur within the time range
        """
        timestamp = self.date_time
        while timestamp<=end:
            if timestamp>=start and timestamp<=end:
                return True
            timestamp = self.change_time(timestamp)
        False
    
    def __str__(self) -> str:
        """Prints out the CalendarArrangement object
        : param self: a CalendarArrangement object
        : return: a String
        """
        recur = ''
        date_time = CalendarTIme(self.date_time)
        if self.recurring == 'Yearly':
            recur = f'Recurs on {date_time.month_lst()} {self.date_time.day} every year.'
        elif self.recurring == 'Monthly':
            recur = f'Recurs on {self.date_time.day} day of every month.'
        elif self.recurring == 'Weekly':
            recur = f'Recurs on every {date_time.weekday_lst()}.'
        elif self.recurring == 'Daily':
            recur = 'Recurs Every day'
        elif self.recurring == 'Hourly':
            recur = 'Recurs every hour.'
        else:
            recur = 'Does not recur.'
        return 'Arrangement\n'+super().__str__()+f'\n{recur}'+'\n'
    
    def write_to_file(self):
        """Writes the CalendarArrangement into a text file in String format
        : param self: a CalendarArrangement object
        : return: a String
        """
        r = self.reminder
        if self.reminder != False:
            r = self.date_time-self.reminder
            r = datetime.datetime.strftime(r,'%m-%d-%Y,%H:%M:%S')
        return 'Arrangement '+f'{self.date_time} '+f'{self.event_details} '+f'{r} '+f'{self.recurring} '
    
