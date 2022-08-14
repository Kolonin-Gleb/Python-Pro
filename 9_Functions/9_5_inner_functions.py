# ВЛОЖЕННЫЕ ФУНКЦИИ, ЗАМЫКАНИЯ
'''
def outer_function(arg):
    num = 5
    # name = 'Timur'
    numbers = [1, 2, 3]
    def inner_function():      # определяем вложенную функцию
        print(arg)
        print(num)
        print(numbers)
    return inner_function      # возвращаем вложенную функцию
        
inner = outer_function('python')

for var in inner.__closure__:
    print(var)
    print(var.cell_contents)

def outer(x):
    def inner():
        return x
    x = None
    return inner

print(outer(10)()) # None
'''

# Функция power()
'''
def power(degree):
    def doit(x):
        return x**degree
    return doit
'''

# Функция generator_square_polynom
'''
def generator_square_polynom(a, b, c):
    def doit(x):
        return a*x**2 + b * x + c
    return doit


f = generator_square_polynom(1, 2, 1)
print(f(5))
# 36
'''

# Функция sourcetemplate
'''
Параметры в строке запроса должны располагаться по алфавиту ключей.

def sourcetemplate(url: str):
    def realization(**kwargs):
        if not kwargs:
            return url
        query_string = ''
        kwargs = dict(sorted(kwargs.items())) # Сортировка словаря по ключам
        for key, value in kwargs.items():
            query_string = f"{query_string}{key}={value}&" 
        query_string = query_string[:-1]
        return f"{url}?{query_string}"
    return realization
'''

# Функция date_formatter()
'''
from datetime import date

def date_formatter(country_code: str):
    def get_d(d: date):
        formats = {
        'ru': '%d.%m.%Y',
        'us': '%m-%d-%Y',
        'ca': '%Y-%m-%d',
        'br': '%d/%m/%Y',
        'fr': '%d.%m.%Y',
        'pt': '%d-%m-%Y',
        }
        return d.strftime(formats[country_code])
    return get_d

date_ru = date_formatter('ru')
print(date_ru(date(2022, 1, 25)))
'''

# Функция sort_priority() 
'''
Функция должна сортировать по неубыванию список чисел values,
делая при этом приоритетной группу чисел из group,
которая должна следовать первой.
'''
def sort_priority(values: list, group):
        global numbers # Бобёр хитёр :D
        # Оставляю в группе только эл., которых нет в значениях и сортирую их
        group = sorted([el for el in group if el in numbers])
        # Расширяю группу приоритета отсортированными значениями, что не являются приоритетными
        group.extend(sorted([val for val in numbers if val not in group]))
        numbers = group
        # print(values)

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)

print(numbers)
# [2, 3, 5, 7, 1, 4, 6, 8]

numbers = [150, 200, 300, 1000, 50, 20000]
sort_priority(numbers, [300, 100, 200])

# print(numbers)
# [200, 300, 50, 150, 1000, 20000]

numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
sort_priority(numbers, (300, 100, 200))

# print(numbers)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

