import calendar
import locale 

# Аттрибуты из модуля calendar
'''
for name in calendar.day_name:
    print(name)

print("_____________________________________")
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

for name in calendar.day_name:
    print(name)

print(calendar.MONDAY)
'''

# Функции модуля calendar
'''
print(calendar.isleap(2020)) # Високосный год
print(calendar.isleap(2021)) # Обычный год

# Матрица - кланедарь на месяц
# Дни, которые не входят в указанный месяц, представлены нулями.
# При этом каждая неделя начинается с понедельника, если не установлено другое функцией ​​setfirstweekday().
print(*calendar.monthcalendar(2021, 9), sep='\n')

print(calendar.month(2021, 9))
'''

# tasks
# step 7
'''
res = []
for _ in range(int(input())):
    res.append(calendar.isleap(int(input())))

print(*res, sep="\n")

# step 8
year, month = input().split()
print(calendar.month(int(year), list(calendar.month_abbr).index(month)))

# step 9
print(list(calendar.day_name)[date.fromisoformat(input()).weekday()])


# step 10
import calendar
year, month_num = input().split()

m_calendar = calendar.monthcalendar(int(year), int(month_num))
total_days = 0
for week in range(len(m_calendar)):
    for day in m_calendar[week]:
        if day != 0:
            total_days += 1

print(total_days)

# Правильное решение
year, number = map(int, input().split())
days = calendar.monthrange(year, number)[1]
print(days)
'''

# step 11
'''
year, month = input().split()
print(calendar.monthrange(int(year), list(calendar.month_name).index(month))[1])
'''

# step 12
'''
import calendar
from datetime import date

def get_days_in_month(year: int, month: str):
    month_num = list(calendar.month_name).index(month)
    dates = []
    for day in range(1, calendar.monthrange(int(year), month_num)[1] + 1):
        dates.append(date(year, month_num, day))
    return dates

print(get_days_in_month(2021, 'December'))
# [date(2021, 12, 1), date(2021, 12, 2), date(2021, 12, 3), ..., date(2021, 12, 30), date(2021, 12, 31)]
'''

# STEP 13
'''

def get_all_mondays(year: int):
    # Первая дата: date(2021, 1, 4)
    dates = []
    for day in range(1, calendar.monthrange(int(year), 0)[1] + 1):
        dates.append(date(year, month_num, day))
    return dates



print(get_all_mondays(2021))
# [date(2021, 1, 4), date(2021, 1, 11), date(2021, 1, 18), ..., date(2021, 12, 20), date(2021, 12, 27)]
'''

# Почему-то не проходит
'''
from datetime import date, timedelta

def get_all_mondays(year):
    d = date(year, 1, 1)                    # January 1st
    d += timedelta(days = d.weekday() - 1)  # First Sunday
    dates = []
    while d.year == year:
        dates.append(d)
        d += timedelta(days = 7)
    return dates


print(get_all_mondays(2021))
'''

