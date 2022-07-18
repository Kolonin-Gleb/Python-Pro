'''
from datetime import date # Импорти типа данных/класса date

my_date = date(1992, 10, 6) # год месяц день

print(my_date)
# print(type(my_date))

print("year = ", my_date.year)
print("month = ", my_date.month)
print("day = ", my_date.day)
'''

# step 20
'''
from datetime import date

def get_min_max(dates: list):
    if dates:
        return (min(dates), max(dates))
    return tuple()
'''

# 21
'''
# Сломается, если даты находятся в разных месяцах
# Чтобы не ломался, когда даты в разных месяцах, их нужно переводить в числа

from datetime import date

def get_date_range(start: date, end: date):
    start = date.toordinal(start)
    end = date.toordinal(end)
    dates = []
    while start <= end:
        dates.append(date.fromordinal(start))
        start += 1 
    return dates

date1 = date(2019, 6, 5)
date2 = date(2019, 6, 5)

print(get_date_range(date1, date2))

# Более элегантное решение

def get_date_range(start, end):
    return [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)]
'''

# 22 
''''''
from datetime import date

def saturdays_between_two_dates(start: date, end: date):
    if start > end:
        start, end = end, start

    return len([d for d in range(start.toordinal(), end.toordinal() + 1) if date.fromordinal(d).isoweekday() == 6])

date1 = date(2018, 7, 13)
date2 = date(2018, 7, 13)

print(saturdays_between_two_dates(date1, date2))

