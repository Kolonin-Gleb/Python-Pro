# Для форматированного вывода даты и времени используется метод strftime()
'''
from datetime import date, time

my_date = date(2021, 8, 10)
my_time = time(7, 18, 34)

print(my_date)                             # вывод в ISO формате
print(my_time)                             # вывод в ISO формате

print(my_date.strftime('%d/%m/%y'))        # форматированный вывод даты
print(my_date.strftime('%A %d, %B %Y'))    # форматированный вывод даты
print(my_time.strftime('%H.%M.%S'))        # форматированный вывод времени
'''

# Преобразование строки в дату и время

# 12
'''
from datetime import date
print(date.fromisoformat(min(input(), input())).strftime('%d-%m (%Y)'))
# 13
from datetime import date

dates = [date.fromisoformat(input()) for _ in range(int(input()))]

for d in sorted(dates):
    print(d.strftime("%d/%m/%Y"))
# 14
from datetime import date

def print_good_dates(dates:list):
    good_dates = []
    for d in dates:
        if d.year == 1992 and d.month + d.day == 29:
            good_dates.append(d)
    for d in sorted(good_dates):
        print(d.strftime('%B %d, %Y'))


dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)
# 15
from datetime import date

def is_correct(day, month, year):
    try:
        date(year, month, day)
        return True
    except:
        return False
'''
# 16
from datetime import date, datetime

dates = []
correct_dates_counter = 0
date_or_end = ''
while True:
    date_or_end = input()
    if date_or_end == 'end':
        break
    try:
        new_date = datetime.strptime(date_or_end, "%d.%m.%Y")
        dates.append('Корректная')
        correct_dates_counter += 1
    except:
        dates.append('Некорректная')

print(*dates, sep='\n')
print(correct_dates_counter)

'''
19.05.2016
05.13.2010
21.12.2012
01.01.1000
32.04.2003
end
'''