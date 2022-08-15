# Модуль typing используется для аннотирования типов.
# Аннотирование не гарантирует, что тип действительно такой.

# Можно указать, какие типы данных содержит коллекция
# Работает в Python 3.9 и выше.
# В более ранних версиях используй import typing
'''
def sum_square(nums: list[int]) -> float: # nums - коллекция типа List, елементы которой имеют тип int
    total = 0
    for i in nums:
        total += i ** 2
    return total
'''

# Аттрибут __annotations__ - просмотр аннотаций аргументов функции
'''
def print_hello(num1: int, num2: int, num3: int) -> float:
    return (num1 + num2 + num3) / 3

print(print_hello.__annotations__)
'''

# Полезные типы модуля typing
'''
Union - аргумент любого из перечисленных типов
Optional - аргумент может иметь значение None
Any - аргумент любого типа. Может быть чем угодно
NoReturn - функция никогда не возращает значение (когда всегда будет вызываться исключение)
'''

'''
def get_digits(number: int | float) -> list[int]:
    return list(map(int, list(str(number).replace('.', ''))))

print(get_digits(16733))
annotations = get_digits.__annotations__
print(annotations['return'])
'''

# Функция должна возвращать словарь, содержащий имя ученика по ключу name и его самую высокую оценку по ключу top_grade.
'''
def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    return {'name':grades['name'], 'top_grade':max(grades['grades'])}
'''

# 
'''
Функция должна изменять переданный список, циклически сдвигая элементы списка на step шагов, и возвращать значение None.
Если step является положительным числом, сдвиг происходит вправо, если отрицательным — влево.
'''

# План
'''
1) Привести шаг к стандартному виду. 
Если он > чем кол. эл, то будет ходить по кругу

2) Пройтись по всем эл. с конца в начало
Каждый эл. записать в другой список по индексу = индекс эл. + step.
    Если индекс эл. + step > длина списка
        индекс эл. + step - len списка

'''
'''
def cyclic_shift(nums: list[int | float], step: int) -> None:
    global numbers
    ans = ['-'] * len(nums)

    if step > len(nums): # Необходимо стандартизировать сдвиг
        while step > len(nums):
            step -= len(nums)
    elif -step > len(nums):
        while step < len(nums):
            step += len(nums)

    for ind, num in enumerate(nums):
        if ind+step >= len(nums):
            ans[ind+step-len(nums)] = num
        else:
            ans[ind+step] = num
    numbers = ans
'''

'''
Функция должна возвращать словарь, ключом в котором является номер строки матрицы,
а значением — список элементов этой строки.

Нумерация строк матрицы в возвращаемом функцией словаре должна начинаться с единицы.
'''

def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    d = {}
    for rowNum in range(1, len(matrix)+1):
        for col in matrix[rowNum-1]:
            d.setdefault(rowNum, []).append(col)
    return d



matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]
print(matrix_to_dict(matrix))
# {1: [5, 6, 7], 2: [8, 3, 2], 3: [4, 9, 8]}

matrix = [[5.1, 6, 7.94]]
print(matrix_to_dict(matrix))
# {1: [5.1, 6, 7.94]}

annotations = matrix_to_dict.__annotations__
print(annotations['return'])
# dict[int, list[int | float]]
