# Конвейеры генераторов - цепочки из генераторов,
# позволяющие производить множество операций без написания сложных циклов обработки.
'''
# Каждый элемент будет генерироваться по очереди на конвеере
n = 10
integers = (i for i in range(1, n + 1))
evens = (i for i in integers if not i % 2)
squared = (i * i for i in evens)
negated = (-i for i in squared)
print(*negated)
'''

# 1. Вывести имя и фамилию самого молодого живого мужчины из Швеции (Swedish).
'''
from collections import namedtuple

Person = namedtuple('Person', ['name', 'nationality', 'sex', 'birth', 'death'])

persons = [Person('E. M. Ashe', 'American', 'male', 1867, 1941),
           Person('Goran Aslin', 'Swedish', 'male', 1980, 0),
           Person('Erik Gunnar Asplund', 'Swedish', 'male', 1885, 1940),
           Person('Genevieve Asse', 'French', 'female', 1949, 0),
           Person('Irene Adler', 'Swedish', 'female', 2005, 0),
           Person('Sergio Asti', 'Italian', 'male', 1926, 0),
           Person('Olof Backman', 'Swedish', 'male', 1999, 0),
           Person('Alyson Hannigan', 'Swedish', 'female', 1940, 1987),
           Person('Dana Atchley', 'American', 'female', 1941, 2000),
           Person('Monika Andersson', 'Swedish', 'female', 1957, 0),
           Person('Shura_Stone', 'Russian', 'male', 2000, 0),
           Person('Jon Bale', 'Swedish', 'male', 1950, 0)]

def alives(persons):
    for pers in persons:
        if pers.death == 0:
            yield pers

def males(persons):
    for pers in persons:
        if pers.sex == 'male':
            yield pers

def swedish(persons):
    for pers in persons:
        if pers.nationality == 'Swedish':
            yield pers

candidates = swedish(males(alives(persons)))

print(max(*candidates).name)
'''

# 2. Функция parse_ranges()
# 1-2,4-4,8-10 => нужно развернуть указанные диапозоны
# Вернуть генератор, порождающий последовательность чисел указанных в диапохонах
'''
def parse_ranges(ranges: str):
    for rang in ranges.split(','):
        a, b = map(int, rang.split('-'))
        while a <= b: # yield from range(a, b + 1)
            yield a
            a += 1

print(*parse_ranges('1-2,4-4,8-10'))
print(*parse_ranges('1-10,2-10'))
print(*parse_ranges('7-32'))
'''

# 3. Функция filter_names()
# вернуть генератор, порождающий max_names имён из списка names игнорируя:
# начинающиеся на ignore_char
# содержащие цифру
'''
def filter_names(names: list, ignore_char: str, max_names: int):
    for name in names:
        if max_names != 0:
            if not ignore_char.lower() == str.lower(name[0]):
                if name.isalpha():
                    yield name
                    max_names -= 1
        else:
            break

data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
print(*filter_names(data, 'D', 3))
'''

# Сокращённые вариант
'''
def filter_names(names: list, ignore_char: str, max_names: int):
    ignore_char = ignore_char.lower()
    filtered_char = (name for name in names if not name.lower().startswith(ignore_char))
    filtered_dig = (name for name in filtered_char if name.isalpha())
    return (name for ind, name in enumerate(filtered_dig) if ind < max_names)
'''

# 4. Инвестиции
# Общая сумма инвестиций в раунде а 
'''
with open('data.csv', 'r', encoding='utf-8') as file:
    file_lines = (line for line in file) # Сбор всех строк файла
    lines_values = (line.rstrip().split(',') for line in file_lines) # Выцепление значений из строк файла
    next(lines_values) # Пропуск строки заголовков
    total = (int(val[1]) for val in lines_values if val[2] == 'a')
    print(sum(total))
'''

# 5. years_days()
# Генератор порождающий все даты в году от заданного года
'''
from datetime import date

def years_days(year: int):
    d = date(year=year, month=1, day=1)
    while d.year == year:
        yield d
        d = date.fromordinal(d.toordinal() + 1) 
'''

# 6. nonempty_lines()
# Вернуть генератор всех НЕПУСТЫХ строк файла без \n
# Если строка > 25 - заменить ...
'''
def nonempty_lines(file: str):
    with open(file, 'r', encoding='utf-8') as f:
        # Чтение с обработкой всех строк
        for line in f:
            if line.strip() != '':
                if len(line) > 25:
                    yield '...'
                else:
                    yield line.rstrip()
'''

# 7. txt_to_dict()
# Вернуть генератор, порождающий последовательность словарей
'''
def txt_to_dict():
    with open('planets.txt', 'r', encoding='utf-8') as file:
        planets = []
        planet = dict()
        file_lines = (line for line in file)
        for line in file_lines:
            if line.strip() != '':
                key, val = line.split(' = ')
                planet[key] = val.rstrip()
            else:
                planets.append(planet)
                planet = dict()
        yield from planets
'''

# Особенности итераторов range

# Функция unique()
# Вернуть генератор порождающий последовательность эл. итерируемого объекта
# без дубликатов в исх. порядке
'''
def unique(iterable):
    uniq = set()
    for el in iterable:
        if el not in uniq:
            uniq.add(el)
            yield el
'''

# Функция stop_on
'''
def stop_on(iterable: iter, obj):
    for el in iterable:
        if el != obj:
            yield el
        else: break
        

numbers = [1, 2, 3, 4, 5]
print(*stop_on(numbers, 4))
'''

# Функция with_previous()
'''
def with_previous(iterable: iter):
    previous = None
    for el in iterable:
        yield (el, previous)
        previous = el
'''
# Функция pairwise()
'''
def pairwise(iterable):
    iterable = iter(iterable)
    current = None
    following = None
    try:
        current = next(iterable)
        following = next(iterable)
        yield (current, following)
        current = following
    except StopIteration:
        if not current:
            return None
        else:
            yield (current, None)

    try:
        for el in iterable:
            following = el
            yield (current, following)
            current = following
    except StopIteration:
        yield (current, None)
    yield (current, None)
'''

# Функция around()
'''
def around(iterable):
    iterable = iter(iterable)
    previous = None
    current = None
    following = None
    try:
        current = next(iterable)
        following = next(iterable)
        yield (None, current, following)
        previous = current
        current = following
    except StopIteration:
        if not current:
            return None
        else:
            yield (None, current, None)

    try:
        for el in iterable:
            following = el
            yield (previous, current, following)
            previous = current
            current = following
    except StopIteration:
        yield (previous, current, None)
    yield (previous, current, None)
'''

# 
