# Модуль itertools - содержит функции для создания итераторов

# Функции порождающие данные
# count(), cycle(), repeat() и т.д.

# count - бесконечный итератор start, step не имеющий stop
'''
import itertools as it
import time

symbols = ['.', '-', "'", '"', "'", '-', '.', '_']

for c in it.cycle(symbols):
    print(c, end='')
    time.sleep(0.05)
'''
# 
'''
from itertools import repeat

beegeek = ['bee', 'geek']
repeater = repeat(beegeek)

print(next(repeater))

beegeek = beegeek + ['imposter'] # Исходный список не был изменён. Был создан новый список и сохранён в beegeek

print(next(repeater))
print(beegeek)
'''

# 1. Функция tabulate
# Вернуть итератор, генерирующий беск.  посл.
# возращаемых значений сначала с арг. 1, затем 2, затем 3 и т.д.
'''
from itertools import count
def tabulate(func):
    counter = count(1, 1)
    while True:
        yield func(next(counter))


func = lambda x: x
values = tabulate(func)

print(next(values))
print(next(values))
'''

# 2. Функция factorials
'''
from itertools import accumulate
import operator

def factorials(n: int):
    yield from accumulate(range(1, n+1), operator.mul)
'''

# 3. Функция alnum_sequence
'''
from itertools import cycle
from string import ascii_uppercase

def alnum_sequence():
    for item in zip(cycle(range(1, 27)), cycle(ascii_uppercase)):
        yield from item
'''

# 4. Функция roundrobin() 
'''
def roundrobin(*args):
    pass
'''




