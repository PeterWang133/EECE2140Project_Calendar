import datetime
from object.c_event import CalendarEvent
from object.c_arrange import CalendarArrangement
from object.c_eventlibrary import EventLibrary
import winsound

# Organizes different methods into a series of main functions, which includes:
# Search by date or date range (Done)
# Add event
# Search event by type (Done)
# Search by keyword (Done)
# Date Countdown (Done)
# Edit an existing event (for reminder type, recurring type, event details, and datetime)
# Update for notification and deadline counttown

Events = EventLibrary()
Events.sort_by_date()


def search_by_date(obj,date):
    d_t = date.split('-')
    d_t.extend([0,0,0])
    da_ti=''
    da_ti = datetime.datetime(year=int(d_t[2]), month=int(d_t[0]), day=int(d_t[1]), hour=d_t[3], minute=d_t[4], second=d_t[5])
    date_dict = obj.get_date_event(da_ti)
    return date_dict

def search_by_daterange(obj,date_start, date_end):
    d_t_st = date_start.split('-')
    d_t_st.extend([0,0,0])
    d_t_ed = date_end.split('-')
    d_t_ed.extend([23,59,59])
    da_ti=''
    da_ti_st = datetime.datetime(year=int(d_t_st[2]), month=int(d_t_st[0]), day=int(d_t_st[1]), hour=d_t_st[3], minute=d_t_st[4], second=d_t_st[5])
    da_ti_ed = datetime.datetime(year=int(d_t_ed[2]), month=int(d_t_ed[0]), day=int(d_t_ed[1]), hour=d_t_ed[3], minute=d_t_ed[4], second=d_t_ed[5])
    date_dict = obj.get_date_range(da_ti_st, da_ti_ed)
    return date_dict

def search_by_daterange_obj(obj:EventLibrary,date_start, date_end):
    d_t_st = date_start.split('-')
    d_t_st.extend([0,0,0])
    d_t_ed = date_end.split('-')
    d_t_ed.extend([23,59,59])
    da_ti=''
    da_ti_st = datetime.datetime(year=int(d_t_st[2]), month=int(d_t_st[0]), day=int(d_t_st[1]), hour=d_t_st[3], minute=d_t_st[4], second=d_t_st[5])
    da_ti_ed = datetime.datetime(year=int(d_t_ed[2]), month=int(d_t_ed[0]), day=int(d_t_ed[1]), hour=d_t_ed[3], minute=d_t_ed[4], second=d_t_ed[5])
    date_dict = obj.get_date_range_obj(da_ti_st, da_ti_ed)
    return date_dict

def search_by_type(obj:EventLibrary,type):
    type_dict = {}
    type_dict = obj.get_event_by_type(type)
    return type_dict

def search_by_keyword(obj, key_word):
    key_dict = obj.get_event_by_keyword(key_word)
    return key_dict

def date_count_down(Event:CalendarEvent, date_time):
    day = Event.date_time-date_time
    return day.days

def edit_event_details(Event:CalendarEvent, details):
    Event.modify_event_details(details)

def edit_event_date(Event:CalendarEvent, date_time):
    Event.modify_datetime(date_time)

def change_notification(Event:CalendarEvent):
    Event.on_or_off()

def arrangement_recurring(Arrangement:CalendarArrangement,recurring_type):
    Arrangement.recurring = recurring_type

def search_and_sort(obj:EventLibrary,date_range, type, key_word, alphabet):
    search_obj = EventLibrary()
    search_obj.event_dict = obj.sort_by_date()
    s=''
    if len(date_range) == 1:
        date_range.append(date_range[0])
    search_obj.event_dict=search_by_daterange(obj, date_range[0], date_range[1])
    if type!='':
        search_obj.event_dict=search_by_type(search_obj, type)
    if key_word!='':
        search_obj.event_dict=search_by_keyword(search_obj, key_word)
    if alphabet==True:
        lst = search_obj.sort_by_alphabet()
        for i in range (len(lst)):
            for e in lst[i]:
                s+=e.__str__()+'\n'
    else:
        s = search_obj.display_all_events()
    return s

def search_and_sort_obj(obj:EventLibrary,date_range, type, key_word):
    search_obj = EventLibrary()
    search_obj.event_dict = obj.sort_by_date()
    if len(date_range) == 1:
        date_range.append(date_range[0])
    search_obj.event_dict=search_by_daterange_obj(obj, date_range[0], date_range[1])
    if type!='':
        search_obj.event_dict=search_by_type(search_obj, type)
    if key_word!='':
        search_obj.event_dict=search_by_keyword(search_obj, key_word)
    return search_obj.event_dict


def play_sound(event:CalendarEvent, current_time):
    if event.notification(current_time) or event.delay_noti(event.delay_time, current_time):
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)


events = EventLibrary() 
