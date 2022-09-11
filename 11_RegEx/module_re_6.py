# search возращает позицию первого удачного поиска.
# from re import search
'''
print(search('super', 'superstition again superstition')) # span(0, 5) - индекс начального и конечного вхождения (невключительно)
print(search('super', 'without')) # None - не найдено

print(search('[a-z]+', '123foFo456'))
print(search('\d+', 'foo.bar'))
'''

# match - начало строки должно совпадать с паттерном
# from re import match
'''
print(match('super', 'superstition'))
print(match('super', 'insuperable'))
'''

# fullmatch - если вся строка соответствует шаблону
# from re import fullmatch
'''
print(fullmatch('\d+', '123foo'))
print(fullmatch('\d+', '123321'))
'''

# Удобно использовать при валидации данных
'''
phone_pattern = r'\d{3}-\d{3}-\d{4}'
print(fullmatch(phone_pattern, '777-888-1234'))
'''

# Полезные методы и атрибуты типа Match

# Метод group() - возращает одну или несколько подгрупп совпадения.
'''
from re import search
# () - вложенное выражение
match = search('(\w+),(\w+),(\w+)', 'foo,bar,baz')

print(match)

print(match.group())  # все группы совпадения
print(match.group(0)) # 0 - тоже все группы совпадения
print(match.group(1)) # 1ая подгруппа

print(match.group(1, 2, 3)) # кортеж из подгрупп
print(match.group(1, 2, 3, 1, 2, 2, 3, 3, 3, 3)) # Можно выводить захваченные группы в любом порядке любое число раз
'''

# Удобство работы с именованными группами
'''
from re import search

match = search('(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'foo,bar,baz')

print(match.group())
print(match.group('w1'))
print(match.group('w1', 'w2', 'w3', 'w2', 'w3'))
'''

# Метод groups() - все захваченные группы в виде кортежа
'''
from re import search

match = search('(\w+),(\w+),(\w+)?', 'foo,bar,') # ? - 0 или более вхождений последней группы
print(match.groups()) # None - группа не участвовала в сопоставлении.
print(match.groups(default='Not detected')) # Результат в случаях, когда не было сопоставления
'''

# Метод groupdict() - словарь всех захваченных именованных групп
'''
from re import search

match = search('(?P<w1>\w+)?,(?P<w2>\w+)?,(?P<w3>\w+)', ',,baz')
print(match.groupdict(default='not_detected'))
'''

# Методы start() и end() - возращают индексы кортежа span (охвата), где было найдено совпадение с RegEx 
# Метод span() - возращает кортеж span (охвата), где было найдено совпадение с RegEx 


# ============================================== Задачки ==============================================
'''
from re import search
match1 = search(r'\w+', 'Hello, Timur') # \w+ = [a-zA-Z]. Запятая и последующие символы не войдут в совпадение
# print(match1)
print(match1.group() if match1 else None)
'''

# Телефонные номера
'''
import sys
import re

pattern = r'\d{1,3}([- ])\d{1,3}\1\d{4,10}'

results = []

for line in sys.stdin:
    line = line.strip()
    res = re.search(pattern, line)

    if res:
        res = line[res.start():res.end()]
        if " " in res:
            res = res.split(" ")
        else:
            res = res.split("-")
        results.append(res)

for res in results:
    print(f"Код страны: {res[0]}, Код города: {res[1]}, Номер: {res[2]}")
'''

# Более элегантный вариант. Использование именованных групп
'''
import re
import sys

pattern = r'(?P<country>\d{1,3})([ -]?)(?P<city>\d{1,3})\2(?P<number>\d{4,10})'

for number in map(str.rstrip, sys.stdin):
    match = re.fullmatch(pattern, number)
    groups = match.groupdict()
    print(f"Код страны: {groups['country']}, Код города: {groups['city']}, Номер: {groups['number']}")
'''

# Онлайн-школа BEEGEEK
'''
import re
import sys

pattern = r'_\d+[a-zA-Z]*_?'
results = []

for login in map(str.rstrip, sys.stdin):
    match = re.fullmatch(pattern, login)
    if match:
        results.append(True)
    else:
        results.append(False)

print(*results, sep='\n')
'''

# Одинаковые слоги
'''
import re
import sys

pattern = r'\b(\w+?)\1\b'
results = []

for word in map(str.rstrip, sys.stdin):
    match = re.fullmatch(pattern, word)
    if match:
        results.append(word)

print(*results, sep='\n')
'''

# Beegeek
'''
'''
# Примечание 2. Строка может одновременно удовлетворять обеим условиям.

import re
import sys

bee_str_pattern = r'.*bee.*bee.*'
geek_str_pattern = r'\bgeek\b'

stats = {"bee_str": 0, "geek_str": 0}


for line in map(str.rstrip, sys.stdin):
    match = re.search(geek_str_pattern, line)
    if match:
        stats["geek_str"] = stats["geek_str"] + 1

    match = re.search(bee_str_pattern, line)
    if match:
        stats["bee_str"] = stats["bee_str"] + 1
    

print(stats["bee_str"])
print(stats["geek_str"])

