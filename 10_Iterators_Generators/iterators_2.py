# Особенности итераторов
# Встроенные функции, порождающие итераторы

'''
non_zero = filter(None, [-2, -1, 0, 1, 2])
positive = map(abs, non_zero)

print(list(non_zero)) # [-2, -1, 1, 2]
print(list(positive)) # []

non_zero = filter(None, [-2, -1, 0, 1, 2])
positive = map(abs, non_zero)

print(list(positive)) # [2, 1, 1, 2]
print(list(non_zero)) # []
'''


# filterfalse
'''
Функция должна работать противоположно функции filter(), то есть возвращать итератор, 
элементами которого являются элементы итерируемого объекта iterable, 
для которых функция predicate вернула значение False.

def filterfalse(predicate, iterable):
    if predicate == None: predicate = bool
    return filter(lambda el: not predicate(el), iterable)
# В этой реализации возращается итератор класса filter
'''

# Транспонирование матрицы
# Через numpy
'''
import numpy as np

def transpose(matrix):
    res = []
    m = np.array(matrix).T
    for row in m:
        res.append(list(row))
    return res
'''
# Через lambda
# transpose = lambda matrix: list(map(list, zip(*matrix)))


# Функция get_min_max() 😎

'''
def get_min_max(data: list):
    if not data: return None
    iter1 = enumerate(data)
    iter2 = enumerate(data)
    return min(iter1, key=lambda el: el[1])[0], max(iter2, key=lambda el: el[1])[0]
'''

# Без enumerate и работы с итератором
# get_min_max = lambda data: (data.index(min(data)), data.index(max(data))) if data !=[] else None

# TODO: Решить позже
# Функция get_min_max() 😳 iterable 
'''
def get_min_max(iterable):
    # Такое решение на сработает, т.к. итерируемый объект может иметь невероятный размер, что не позволит сохранить его в память
    collection = list(iterable)
    if not collection: return None
    return min(collection), max(collection)
'''


# TODO: Решить позже
# Функция starmap()
'''
persons = [('Timur', 'Guev'), ('Arthur', 'Kharisov')]
full_names = map(lambda tup: tup[0] + ' ' + tup[1], persons)

print(list(full_names))
'''

'''
возвращать итератор, элементами которого являются элементы итерируемого объекта iterable,
к которым была применена функция func, с единственным отличием:
func должна принимать не один аргумент — коллекцию (элемент iterable),
а каждый элемент этой коллекции в качестве самостоятельного аргумента.

def starmap(func, iterable):
    return map(func, iterable)


pairs = [(1, 3), (2, 5), (6, 4)]
print(*starmap(lambda a, b: a + b, pairs))
# 4 7 10

points = [(1, 1, 1), (1, 1, 2), (2, 2, 3)]
print(*starmap(lambda x, y, z: x * y * z, points))
# 1 2 12
'''


