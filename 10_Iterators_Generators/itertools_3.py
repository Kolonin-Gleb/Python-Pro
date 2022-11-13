# Функции объединяющие и разделяющие данные
'''
chain()
chain.from_iterable()
zip_longest()
tee()
'''

# Функция sum_of_digits()
# Необходимо вернуть сумму цифр во всех числах
'''
def sum_of_digits(iterable):
    total = 0
    for el in iterable:
        for dig in str(el):
            total += int(dig)
    
    return total
'''
# Другой вариант
'''
from itertools import chain

def sum_of_digits(iterable):
    tmp = map(str, iterable)
    return sum(map(int, chain.from_iterable(tmp)))
'''
# 
''''''

# Функция is_rising()
'''
def is_rising(iterable):
    iterable = iter(iterable)
    prev = next(iterable)
    for el in iterable:
        if prev < el:
            prev = el
        else:
            return False
    return True
'''

# Функция max_pair()
'''
'''

