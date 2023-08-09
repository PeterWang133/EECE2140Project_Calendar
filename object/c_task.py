from object.c_event import CalendarEvent
import datetime

class CalendarTask(CalendarEvent):
    def __init__(self, date_time: datetime, event_details: str, reminder) -> None:
        super().__init__(date_time, event_details, reminder)
        self.reminder = reminder

    def __str__(self) -> str:
        return f'Task\n{super().__str__()}\n'