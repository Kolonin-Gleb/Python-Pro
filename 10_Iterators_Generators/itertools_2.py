# Функции фильтрующие данные
'''
Функции dropwhile()
Функции takewhile()
Функции filterfalse()
Функции compress()
Функция islice()
'''

'''
from itertools import filterfalse

objects = [True, False, 'True', 'False', [], ()]
print(*filterfalse(None, objects))
'''

# Функция drop_while_negative()
'''
from itertools import dropwhile

def drop_while_negative(iterable):
    yield from dropwhile(lambda x: x < 0, iterable)
'''

# Функция drop_this()
'''
def drop_this(iterable, obj):
    iterable = iter(iterable)
    for el in iterable:
        if el != obj:
            yield el
            yield from iterable
'''
'''
from itertools import dropwhile

def drop_this(iterable, obj):
    yield from dropwhile(lambda el: el == obj, iterable)
'''

# Функция first_true()
'''
def first_true(iterable, predicate):
    if not predicate:
        predicate = bool
    for el in iterable:
        if predicate(el):
            return el
'''

# Функция take()
'''
from itertools import islice

def take(iterable, n):
    yield from islice(iterable, n)
'''

# Функция take_nth()
'''
def take_nth(iterable, n: int):
    for num, el in enumerate(iterable, 1):
        if num == n:
            return el
        elif num > n:
            return None
'''

# first_largest
'''
def first_largest(iterable, number: int):
    for ind, el in enumerate(iterable, 0):
        if el > number:
            return ind
    return -1
'''
