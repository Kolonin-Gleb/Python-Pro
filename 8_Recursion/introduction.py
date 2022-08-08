# Рекурсивная функция с условием выхода
'''
def message(times):
    if times > 0:
        print('Это рекурсивная функция')
        message(times - 1)
        print(times) # Когда рекурсивная функция достигнет дна поток управления будет возращаться назад
        # Как бы из прошлого в будущее

message(5)
'''
# Глубина рекурсии - число раз, что функция вызывает саму себя.
# Здесь функция имеет глубину 5 (исходный раз - она вызывается внешне)


# Задачи
'''
def traffic(n):
    if n > 0:
        print("Не парковаться")
        traffic(n - 1)

traffic(5)
'''
'''
def print100():
    def printik(n):
        if n <= 100:
            print(n)
            printik(n + 1)
    printik(1)
print100()
'''
'''
numbers = [243, -279, 395, 130, 89, 269, 861, 669, 939, 367, -46, 710, 841, -280, -244, 274, -132, 273, 418, 432, -341, 437, 360, 960, 195, 792, 106, 461, -35, 980, -80, 540, -358, 69, -26, -416, 597, 96, 533, 232, 755, 894, 331, 323, -383, -386, 231, 436, 553, 967, 166, -151, 772, 434, 325, 301, 275, 431, 556, 728, 558, 702, 463, 127, 984, 212, 876, -287, -16, -177, 577, 604, 116, 500, 653, 669, 916, 802, 817, 762, -210, -353, 144, -351, 777, 805, 692, 22, -303, 249, 190, 411, 236, -274, 174, 380, 71, 124, -85, 430]

def printLst(numbers: list):
    def printik(index):
        if index < len(numbers):
            print(f"Элемент {index}: {numbers[index]}")
            printik(index + 1)
    printik(0)

printLst(numbers)
'''
# Обратынй порядок
'''
def recursion():
    digit = int(input())
    if digit != 0:
        recursion()
    print(digit)

recursion()
'''

# Функция triangle()
'''
def triangle(h: int):
    if h > 0:
        stars, step = 1, 1
        def printik(stars, step):
            print(' '*(h - step) + '*'*stars)
            if step < h:
                printik(stars+2, step+1)
        printik(stars, step)

triangle(5)
'''

# sandglass
'''
def sandglass():
    stars, step = 16, 0
    def printik(stars, step):
        print(' '*(step) + '*'*(stars-step) )
        if step <= 14:
            printik(stars-4, step+2)
            print(' '*(step - stars) + '*'*stars)
    printik(stars, step)

sandglass()

print("1111111111111111")
print("  222222222222")
print("    33333333")
print("      4444")
print("    33333333")
print("  222222222222")
print("1111111111111111")
'''

# print_digits()
'''
def print_digits(number: int):
    number = str(number)
    length = len(number)
    
    def printik(index):
        if index >=0:
            print(number[index])
            printik(index-1)
    printik(length-1)

print_digits(12345)
'''
'''
def print_digits(n):
    print(n % 10)
    if n >= 10:
        print_digits(n // 10)
'''
# 
'''
def print_digits(number: int):
    number = str(number)
    length = len(number)
    
    def printik(index):
        if index < length:
            print(number[index])
            printik(index+1)
    printik(0)

print_digits(12345)
'''

# Рекурсия Часть 3
'''

def digits_counter(num: int):
    return len(str(num))

print(digits_counter(142))

'''

# print(sum( [int(num) for num in input()] ))
'''

def range_sum(lst: list, start, end):
    return sum(lst[start:end+1])

print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
# 30
'''

'''
def get_pow(num, p):
    return num ** p

print(get_pow(5, 2))
'''

'''
def recursive_sum(a, b):
    return a + b

print(recursive_sum(10, 22))
'''

'''
from math import log

def is_power(n):
    Logn = log(n, 2)
    if (Logn == int(Logn)):
        return True
    else:
        return False

print(is_power(512))
'''

