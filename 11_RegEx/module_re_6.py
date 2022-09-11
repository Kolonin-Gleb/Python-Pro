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
import re
import sys

# Может подходить разная регулярка в зависимости от используемой функции (search/fullmatch)
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
'''

# Popularity
'''
import re
import sys

# Может подходить разная регулярка в зависимости от используемой функции (search/fullmatch)
pattern1 = r'^beegeek.*beegeek$|^beegeek$'
pattern2 = r'^beegeek.*|.*beegeek$'
pattern3 = r'.+beegeek.+'

score = 0

for line in map(str.rstrip, sys.stdin):
    if re.fullmatch(pattern1, line):
        score += 3
    elif re.fullmatch(pattern2, line):
        score += 2
    elif re.fullmatch(pattern3, line):
        score += 1

print(score)
'''


# Флаги

import re

# Флаг re.IGNORECASE - игнорирование регистра
'''
match3 = re.search('a+', 'aaaAAA', re.IGNORECASE)
match4 = re.search('A+', 'aaaAAA', re.I)
print(match3)
print(match4)
'''

# Флаг re.MULTILINE - учитывание символа \n внутри строки, при использовании ^ и $
'''
text = 'foo\nbar\nbaz'

print("ПОИСК БЕЗ ФЛАГА")
print(re.search('^foo', text))
print(re.search('^bar', text))
print(re.search('^baz', text))
print(re.search('foo$', text))
print(re.search('bar$', text))
print(re.search('baz$', text))
print()

print("ПОИСК C ФЛАГОМ")
print(re.search('^foo', text, re.MULTILINE))
print(re.search('^bar', text, re.MULTILINE))
print(re.search('^baz', text, re.MULTILINE))
print(re.search('foo$', text, re.M))
print(re.search('bar$', text, re.M))
print(re.search('baz$', text, re.M))
'''

# Флаг re.DOTALL - включает символ переноса строки в то, что захватывает метасимвол .
'''
print(re.search('foo.bar', 'foo\nbar'))
print(re.search('foo.bar', 'foo\nbar', re.DOTALL))
print(re.search('foo.bar', 'foo\nbar', re.S))
'''

# Комбинирование флагов - |
'''
match = re.search('^bar', 'FOO\nBAR\nBAZ', re.I | re.M)
print(match)
'''

# Функция escape() - получение строки с экранированием метасимволов
'''
match = re.escape('http://www.stepik.org')
print(match)
'''

# Флаг verbose - добавление комментариев
"""
import re
text = 'Десятичное число равно 123.7'
match = re.search('''\d +  # целая часть
                     \.    # десятичная точка
                     \d *  # дробная часть''', text, re.VERBOSE)

print(match)
"""

# Существуют и другие флаги


# Уважение
'''
import re
print(bool(re.match("^Здравствуйте|^Доброе утро|^Добрый день|^Добрый вечер", input(), re.IGNORECASE)))
'''

# Социальные сети = подсчёт beegeek без учёта регистра
'''
import re, sys

pattern = r'.*beegeek.*'
score = 0

for line in map(str.rstrip, sys.stdin):
    if re.search(pattern, line, re.IGNORECASE):
        score += 1

print(score)
'''



