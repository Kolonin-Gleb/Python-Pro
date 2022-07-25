# Преобразование строки в дату-время

# 16
'''
from datetime import date, time, datetime

dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
         date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24), 
         date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]

times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59), 
         time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2), 
         time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]

dts = [datetime.combine(d, t) for d, t in zip(dates, times)]
print(*sorted(dts, key= lambda dt: dt.second), sep='\n')
'''

# 17
'''
'''

from datetime import datetime, timedelta

data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'), 
        'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'), 
        'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'), 
        'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'), 
        'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'), 
        'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'), 
        'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'), 
        'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'), 
        'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'), 
        'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'), 
        'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}
dt_pattern = '%d.%m.%Y %H:%M:%S'

fastest = timedelta(weeks=999) # вывел имя ученика, который затратил на решение домашнего задания меньше всего времени.
champion = ''

for name, values in data.items():
    delta = datetime.strptime(values[1], dt_pattern) - datetime.strptime(values[0], dt_pattern)
    if delta < fastest:
        fastest = delta
        champion = name

print(champion)