#15
'''
from datetime import date, datetime

cur_date = (datetime.strptime(input(), '%d.%m.%Y').date())

print(date.fromordinal(cur_date.toordinal()-1).strftime('%d.%m.%Y'))
print(date.fromordinal(cur_date.toordinal()+1).strftime('%d.%m.%Y'))
#16
from datetime import time

t = time.fromisoformat(input())
seconds = t.hour * 3600 + t.minute * 60 + t.second
print(seconds)
'''

#17 SAD
'''
from datetime import time, timedelta

t = time.fromisoformat(input())
alarm_time = t.hour * 3600 + t.minute * 60 + t.second + int(input())
alarm_time = timedelta(seconds = alarm_time)

if alarm_time.days != 0:
    alarm_time = str(alarm_time)
    alarm_time = alarm_time[alarm_time.find(',')+2:]
    if alarm_time == '0:00:00':
        print('00:00:00')
    else:
        print(alarm_time)
else:
    alarm_time = str(alarm_time)
    if len(alarm_time) != 8:
        print('0' + alarm_time)
    else:
        print(alarm_time)
'''

# Нормальное решение
'''
from datetime import datetime, timedelta

pattern = '%H:%M:%S' # Формат в котором получаю время

dt = datetime.strptime(input(), pattern) + timedelta(seconds=int(input())) # Результатом будет объект типа datetime
print(dt.strftime(pattern))
'''
