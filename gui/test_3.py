import datetime

time_delay = datetime.timedelta(days=5)
d = datetime.datetime.today()
d_later = d+datetime.timedelta(days=5)
read_delay = ''

with open(file='Testing.txt', mode='w', encoding='utf8') as f:
    s = d_later.strftime('%m-%d-%Y %H:%M:%S')
    print(s, file=f)

with open(file='Testing.txt', mode='r', encoding='utf8') as f:
    s=f.readline()
    s=s.rstrip()
    print(s)
    read_delay = datetime.datetime.strptime(s,"%m-%d-%Y %H:%M:%S")

#delta = datetime.timedelta(hours=read_delay.hour, minutes=read_delay.minute, seconds=read_delay.second)
#print(delta)