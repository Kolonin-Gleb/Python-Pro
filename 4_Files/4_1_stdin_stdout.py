# import sys

# Потоковый ввод
'''
# Будер работать как эхо
for line in sys.stdin:
    print(line.strip('\n'))

# Работа с потоковым вводом sys.stdin - полезна, когда неизвестен момент остановки ввода данных пользователем 
'''

# Потоковый вывод
'''
print('Hello')
sys.stdout.write('Hello') # Но тут нет переноса строки 
# Этот код равносилен, т.к. print передаёт данные для печати потоковому выводу

# sys.stdout.write(24) # Приведёт к ошибке. В поток вывода можно передавать только СТРОКИ
'''

# tasks

# step 10 Обратный порядок
'''
import sys
data = [line[::-1].strip() for line in sys.stdin]
print(*data, sep='\n')
'''

# step 11 Разница между датами
# Будер работать как эхо
'''
import sys
from datetime import datetime

dates = [datetime.fromisoformat(line.strip('\n')).date() for line in sys.stdin]
print(max(dates).toordinal() - min(dates).toordinal())
'''

# step 12 Лемма о трёх носках
'''
import sys

players_socks = {'Анри': 0, 'Дима': 0}

for turn, line in enumerate(sys.stdin):
    socks = int(line)

if turn % 2 == 0: #Чётный ход - Анри последний
    if socks % 2 == 0:
        print("Анри")
    else:
        print("Дима")
else: # Нечётный ход - Дима последний
    if socks % 2 == 0:
        print("Дима")
    else:
        print("Анри")
'''
# Более элегантное решение
'''
import sys # Т.к. не знаю, когда прекратится ввод данных

data = [int(x) for x in sys.stdin] # Сохраняю вводимые числа в список
if (len(data)-1) % 2 == 0: #Чётный ход - Анри последний
    print('Анри' if data[-1] % 2 == 0 else 'Дима')
else: # Нечётный ход - Дима последний
    print('Дима' if data[-1] % 2 == 0 else 'Анри')
'''

# step 13 Урок статистики
'''
import sys

heights = [int(x) for x in sys.stdin]

if heights:
    print(f"Рост самого низкого ученика: {min(heights)}")
    print(f"Рост самого высокого ученика: {max(heights)}")
    print(f"Средний рост: {sum(heights) / len(heights)}")
else:
    print("нет учеников")
'''

# step 14 Комментатор
'''
import sys

lines = [line for line in sys.stdin]
clear_comments = 0

for line in lines:
    for letter in line:
        if letter == ' ': continue
        elif letter == '#':
            clear_comments += 1
        else:
            break

print(clear_comments)
'''

# step 15 Без комментариев
# Почему-то не проходит
'''
import sys
code = [line for line in sys.stdin if line.strip().find('#') != 0]
print(*code, sep='')
'''

# step 16 Панорамное агенство
'''

import sys

news = [line.strip() for line in sys.stdin]
category = news.pop(-1) # Забираю последнюю запись как категорию из списка новостей
# Новости выбранной категории
category_news = [line for line in news if line.find(category) != -1]
# Разбиение записи
category_news = [line.split(' / ') for line in category_news]
# Сортировка новостей по достоверности и алфавиту
category_news.sort(key= lambda lst: (float(lst[2]), lst[0]))

for new in category_news:
    print(new[0])
'''

# step 17 Это точно Python?
'''
import sys
from datetime import datetime
dates = [datetime.strptime(line.strip('\n'), "%d.%m.%Y") for line in sys.stdin]

# Если имеется 2 одинаковые даты то это сразу MIX. Т.к. порядок должен быть жёстким
unique_dates = set(dates)
if len(unique_dates) != len(dates):
    print("MIX")
elif dates == sorted(dates): # по возрастанию
    print("ASC")
elif dates == sorted(dates, reverse=True): # по убыванию
    print("DESC")
else:
    print("MIX")
'''

# step 18 Гуру прогрессий
'''
import sys

def is_arithmetic(l):
    delta = l[1] - l[0]
    for index in range(len(l) - 1):
        if not (l[index + 1] - l[index] == delta):
             return False
    return True

def is_geometric(li):
    if len(li) <= 1:
        return True
    # Calculate ratio
    ratio = li[1]/float(li[0])
    # Check the ratio of the remaining
    for i in range(1, len(li)):
        if li[i]/float(li[i-1]) != ratio: 
            return False
    return True 

nums = [int(num) for num in sys.stdin]

if is_arithmetic(nums):
    print("Арифметическая прогрессия")
elif is_geometric(nums):
    print("Геометрическая прогрессия")
else:
    print("Не прогрессия")
'''

# 
''''''

