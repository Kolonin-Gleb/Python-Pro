# Генераторы в Python делятся на 2 группы:
'''
1) Функции генераторы - рассматриваются тут
2) Выражения генераторы - рассматриваются в след. уроке
'''

# Функции генераторы - функция, возвращающая итератор. Использует yield вместо return
# Функция генератор сохраняет лок. переменные от вызова к вызову. Т.е. явл. Возобновляемой функцией.

########################################## Пример функции-генератора

'''
def generate_ints(n):
    for num in range(n):
        yield num

generator1 = generate_ints(5) # Создание генератора
print(type(generator1)) 

print(next(generator1))
print(next(generator1))
print(next(generator1))
print(next(generator1))
print(next(generator1))
'''

# Генератор - это итератор, создующий значения передаваемые в yeild
# Можно описать класс собственного генератора
'''
class GenerateInts:
    def __init__(self, n) -> None:
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == self.n:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

iterator2 = GenerateInts(4)

for num in iterator2:
    print(num)
'''

# Генераторная-функция simple_sequence()
# Генерировать бесконечную последовательность с 1
# Где каждое число встречается столько раз, каково оно
'''
def simple_sequence():
    counter = 0
    val = 1
    while True:
        while counter != val:
            yield val
            counter += 1
        counter = 0
        val += 1
'''

# Генераторная-функция alternating_sequence()
'''
def alternating_sequence(count = None):
    val = 1
    if count:
        for _ in range(count):
            yield val
            val = abs(val) + 1
            if val % 2 == 0:
                val = -val
        return StopIteration
    while True:
        yield val
        val = abs(val) + 1
        if val % 2 == 0:
            val = -val
'''

# Функция primes()
# Порождает последовательность простых числе от left до right
# Определить является ли число простым можно исп. алгоритм Решето Эратосфена
# Простое число - число деляющиеся без остатка только на себя и на 1 (кроме 1)

"""
def eratosphene(maximum):
    # список заполняется значениями от 0 до n
    a = []
    for i in range(maximum + 1):
        a.append(i)
    
    ''' В списке a индекс - это число. А его значение 0 - составное, 1 - простое '''

    # Ноль и Один - не считают простым числом Т.е. они составные
    a[1] = 0
    
    # начинаем с 3-го элемента, т.е. 2ки
    i = 2
    while i <= maximum:
        # Если значение предыдущей ячейки != 0,
        # в текущей ячейке содержится простое число.
        if a[i] != 0:
            # первое кратное ему
            # будет в два раза больше
            j = i + i
            while j <= maximum:
                # это число составное, поэтому заменяем его нулем
                a[j] = 0
                # переходим к следующему числу, которое кратно i
                # (оно на i больше)
                j = j + i
        i += 1
    
    # избавляемся от всех нулей 
    a = [el for el in a if el != 0]
    return a

def primes(left: int, right: int):
    primary = eratosphene(right)

    # Беру часть простых чисел в заданном диапозоне
    for i in range(len(primary)):
        if primary[i] >= left:
            yield primary[i]


generator = primes(1, 15)
print(*generator)
# 2 3 5 7 11 13

generator = primes(6, 36)

print(next(generator))
print(next(generator))
# 7
# 11
"""

# Функция reverse()
'''
def reverse(sequence):
    for elem in reversed(sequence):
        yield elem
'''

# Функция dates()
'''
from datetime import date
from math import inf

def dates(start: date, count = None):
    if not count:
        count = inf
    
    start = start.toordinal() - 1
    while count > 0: # Пока не произойдёт ошибка получения максимальной даты
        start += 1
        count -= 1
        try:
            yield date.fromordinal(start)
        except ValueError: # Ошибка получения максимальной даты
            break
'''

# Функция card_deck()
# Порождает генератор колоды без масти suit
'''
def card_deck(suit: str):
    card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    card_mast = ["пик", "треф", "бубен", "червей"]
    card_mast.remove(suit)

    while True:
        for mast in card_mast:
            for card in card_values:
                yield f"{card} {mast}"
'''

# yield from (*iterable) - конструкция yiled from
# совмещает в себе функционал yield и for
# Удобно применять, для создания субгенераторов
'''
def is_digit_palindrome(digit: int):
    digit = str(digit)

    if digit[0::] == digit[::-1]:
        return True
    return False

def palindromes():
    cur_val = 1
    while True:
        if is_digit_palindrome(cur_val):
            yield cur_val
        cur_val += 1
'''

# Функция flatten
'''
def flatten(nested_lists: list):
    for el_or_lst in nested_lists:
        if type(el_or_lst) != list:
            yield el_or_lst
        else:
            yield from flatten(el_or_lst)

generator = flatten([[1, 2], [[3]], [[4], 5]])

print(*generator)
'''

# 
'''
'''

