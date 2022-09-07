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
План:

Очевидно нужно использовать stdin
'''

