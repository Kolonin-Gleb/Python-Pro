# Генераторы в Python делятся на 2 группы:
'''
1) Функции генераторы - рассматриваются в пред. уроке
2) Выражения генераторы - рассматриваются тут
'''


# Генератор списка - выполняется сразу и полностью. 
# Полученный список целиком хранится в памяти
'''
from sys import getsizeof

numbers = [1, 9, 8, 7, 90, -56, -34, 56, 100, 90, 2, 8]

even_numbers = [num for num in numbers if num % 2 == 0]

print(type(even_numbers)) # list
print(even_numbers) # 8 90 -56 -34 56 100 90 2 8
print(getsizeof(even_numbers)) # 192 байта
'''


'''
# Генераторное выражение - внутри ()
# Будет производить вычисления только при обращении
from sys import getsizeof

numbers = [1, 9, 8, 7, 90, -56, -34, 56, 100, 90, 2, 8]

# используем круглые скобки
even_numbers = (num for num in numbers if num % 2 == 0)

print(type(even_numbers)) # <class 'generator'>
print(even_numbers) # <generator object <genexpr> at 0x00000209E9C02B48>
print(getsizeof(even_numbers)) # 120
'''


# Функция cubes_of_odds()
'''
def cubes_of_odd(iterable):
    for number in iterable:
        if number % 2:
            yield number ** 3
'''

# Генераторная функция
'''
def is_prime(n):
	if n == 1: return False

	for i in range(2, n):
		if n % i == 0:
			return False
	return True
'''
# Генераторное выражение в функции
'''
def is_prime(n):
	return n != 1 and all(n % i != 0 for i in range(2, n))
'''

# Функция count_iterable()
'''
def count_iterable(iterable):
	return sum(1 for _ in iterable)
'''

# Функция all_together()
# генератор, порождающий каждый элемент всех переданных итерируемых объектов: сначала все элементы первого итерируемого объекта, затем второго, и так далее.
'''
def all_together(*args_iterables):
	for iterable in args_iterables:
		yield from iterable
'''

# Функция interleave()
'''
def interleave(*args):
	zip_obj = zip(*args)
	for els_from_iterables in zip_obj:
		yield from els_from_iterables


numbers = [1, 2, 3]
squares = [1, 4, 9]
qubes = [1, 8, 27]

print(*interleave(numbers, squares, qubes))
'''
