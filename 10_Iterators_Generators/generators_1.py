# Генераторы в Python делятся на 2 группы:
'''
1) Функции генераторы
2) Выражения генераторы
'''

# Функции генераторы - функция, возвращающая итератор. Использует yield вместо return
# Функция генератор сохраняет лок. переменные от вызова к вызову. Т.е. явл. Возобновляемой функцией.

# Пример функции-генератора

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

# 
'''
'''

