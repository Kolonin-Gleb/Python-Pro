'''
iterator = iter(lambda: 2, 10)
print(next(iterator) + next(iterator))
# 4
'''

# Собственный бесконечный итератор
'''
infinite_love = iter(lambda: 'i love beegeek!', -1)

for i in range(5):
    print(next(infinite_love))
'''

# is_iterable
'''
Функция должна возвращать True, если объект obj является итерируемым объектом, или False в противном случае.

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except:
        return False

print(is_iterable(18731))
# False

print(is_iterable('18731'))
# True
'''

# Альтернатива. Проверка на наличие атрибута
'''
def is_iterable(obj):
    return "__iter__" in dir(obj) # У итерируемого объекта должен быть аттрибут __iter__
'''

# is_iterator
'''
def is_iterator(obj):
    return "__next__" in dir(obj) # У объекта итератора должен быть аттрибут __next__
'''

# random_numbers()
'''
Функция должна возвращать итератор, генерирующий бесконечную последовательность
случайных целых чисел в диапазоне от left до right включительно.
'''

from random import randint

def random_numbers(left: int, right: int):
    return iter(lambda: randint(left, right), 'exit')

iterator = random_numbers(1, 1)

print(next(iterator))
print(next(iterator))
# 1
# 1

iterator = random_numbers(1, 10)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
# True
# True
# True

