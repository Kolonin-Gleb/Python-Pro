# Создание собственных итераторов
'''
Любой итератор должен:
1) Иметь __next__()
2) Иметь __iter__()
=> Нужно создать класс, что будет содержать эти методы
'''

# Создание итератора выдающего последовательность от low до high с шагом 1
'''
class Counter:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    # Возврат ссылки итератором на самого себя
    def __iter__(self):
        return self

    def __next__(self):
        if self.low > self.high:
            raise StopIteration
        else:
            self.low += 1 # Перемещение на следующую позицию
            return self.low - 1 # Возврат информации, что тек. позицию отработали

counter1 = Counter(3, 10) # Инициализация итератора

for i in counter1: # Неявный вызов __next__()
    print(i)

counter2 = Counter(100, 103)
# Явный вызов __next__()
print(next(counter2))
print(next(counter2))
print(next(counter2))
print(next(counter2))
'''


# Итераторы хранят ссылки, на итерируемые объекты, на основе которых они создавались
# Тонкости изменения итерируемого объекта итератора
'''
numbers = [1, 2, 3, 4, 5]

iterator = iter(numbers)

next(iterator) # Считывание 1
next(iterator) # Считывание 2

del numbers[0] # Удаление 3
del numbers[1] # Удаление 4

print(next(iterator)) # Вывод 5
'''

# С подвохом
'''
numbers = [1, 2, 3, 4, 5]

for i in numbers:
    del numbers[0]
    print(i)
'''

# Итератор BoundedRepeater
'''
class BoundedRepeater:
    def __init__(self, object, times: int):
        self.object = object
        self.times = times
        self.cur = 0 # Вспомогательный счётчик

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur < self.times:
            self.cur += 1
            return self.object
        else:
            raise StopIteration
'''

# Итератор Square
'''
class Square:
    def __init__(self, n: int):
        self.sequence = [num**2 for num in range(1, n+1)]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.sequence.pop(0)
        except:
            raise StopIteration
'''

# Итератор Fibonacci
'''
'''
# Итератор класса Fibonacci должен генерировать бесконечную последовательность чисел Фибоначчи, начиная с 1.

class Fibonacci:
    def __init__(self):
        self.el1 = 1
        self.el2 = 1
        self.called_times = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.called_times < 3:
            self.called_times += 1
            return self.el1
        res = self.el1 + self.el2
        self.el1 = self.el2
        self.el2 = res
        return res


fibonacci = Fibonacci()

print(next(fibonacci))
# 1

fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
# 1
# 1
# 2
# 3

