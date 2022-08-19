# В Python существует 2 типа итерируемых объектов
# - итераторы
# - коллекции и последовательности

# Коллекция - набор значений с возможностью обращаться к этим значениям,
# а также применять специальные функции и методы, зависящие от типа коллекции.

# Примеры коллекций: set, dict, tuple, str, list, frozenset

# Последовательность - коллекция, эл. которой пронумерованы индексами и упорядочены как-либо.

# Примеры последовательностей: str, tuple, list

'''
numbers = [1, 2, 3]

iterator = iter(numbers) # Создание итератора из списка

print(iterator)

# Проход по эл. итератора
print(next(iterator))
print(next(iterator))
print(next(iterator))

# В итераторах нельзя запрашивать эл. по индексу
'''

# Функции высшего порядка возращают объекты-итераторы
'''
print(next(enumerate('beegeek')))
# print(next([1, 2, 3, 4, 5])) # Не итератор
# print(next('beegeek')) # Не итератор
# print(next(range(10))) # Не итератор
print(next(map(str.upper, 'beegeek')))
# print(next((1, 2, 3, 4, 5))) # Не итератор
print(next(filter(None, '11010111')))
# print(next({'bee': 1, 'geek': 2})) # Не итератор
# print(next({1, 2, 3, 4, 5})) # Не итератор
print(next(zip('bee', 'geek')))
'''

# Итерируемые объекты, но не итераторы:
'''
# print(next({'bee': 1, 'geek': 2})) # Словарь
# print(next({1, 2, 3, 4, 5})) # Множество
# print(next((1, 2, 3, 4, 5))) # Кортеж
'''

# Объектов-иттераторов не имеет аттрибута len => не работают с функцией len
'''
letters = iter('beegeek')
print(len(letters))

nums = iter(range(100))
print(len(nums))
'''

'''
from sys import getsizeof

# Будут созданы объекты схожие с итераторами.
# Они не хранят все значения диапазона, а генерируют их по необх.
numbers1 = range(10)
numbers2 = range(10000000)

size1 = getsizeof(numbers1)
size2 = getsizeof(numbers2)

print(size1 == size2) # Имеют одинаковый размер в памяти
'''
