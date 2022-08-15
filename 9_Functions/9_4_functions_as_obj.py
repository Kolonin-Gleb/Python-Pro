# ФУНКЦИИ КАК ОБЪЕКТЫ

"""
def numbers_sum(elems: list):
    '''Принимает список и возвращает сумму его чисел (int, float),\nигнорируя нечисловые объекты. 0 - если в списке чисел нет.'''
    return sum(filter(lambda el: type(el) == float or type(el) == int, elems))
"""

# Новый print
# Сделал через декоратор
'''
def upper(func):
    def wrapper(*args, sep=" ", end='\n'):
        args = [str(arg).upper() if type(arg) == str else arg for arg in args]
        return func(*args, sep=sep.upper(), end=end.upper())
    return wrapper

old_print = print
print = upper(print) # Переопределение функции

words = [['black', 'white', 'grey', 'black-1', 'white-1', 'python']]
print(*words, sep=' to ', end=' LOVE')
'''

# BLACK TO WHITE TO GREY TO BLACK-1 TO WHITE-1 TO PYTHON LOVE

# ПОЛЬЗОВАТЕЛЬСКИЕ АТТРИБУТЫ ФУНКЦИЙ
'''
# Можно использовать словарь аттрибутов функции, для кеширования уже вычисленных значений
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
def fib(num):
    if num < 2:
        return num
    if num not in fib.__dict__:
        fib.num = fib(num - 1) + fib(num - 2)
    return fib.num

print(fib(6))
'''

# Функция Polynom
'''
def polynom(x: float):
    if not polynom.__dict__:
        polynom.values = set()
    polynom.values.add(x**2 + 1)
    return x**2 + 1

def polynom(x: int)->int:
    polynom.__dict__.setdefault('values', set()).add(x ** 2 + 1)
    return x ** 2 + 1
'''

# Функция remove_marks
"""
def remove_marks(text: str, marks: str):
    '''возвращать строку text, предварительно удалив из нее все символы, перечисленные в строке marks'''
    remove_marks.__dict__.setdefault('count', 0)
    remove_marks.count += 1

    for mark in marks:
        text = text.replace(mark, '')

    return text
remove_marks.__dict__.setdefault('count', 0)

# text = 'Hi! Will we go together?'
# print(remove_marks(text, '!?'))
# print(remove_marks.count)
"""

# 
'''
'''

