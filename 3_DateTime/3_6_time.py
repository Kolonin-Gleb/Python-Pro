
# step 10
'''
import time

def calculate_it(func, *args):
    start_time = time.monotonic()
    res = func(*args)
    end_time = time.monotonic()
    return (res, end_time - start_time)

def func(a, b, c):
    time.sleep(3)
    return a + b + c

print(calculate_it(func, 1, 2, 3))
'''

# step 11
import time

def get_the_fastest_func(funcs: list, arg):
    best_time = 999999
    best_func = None
    for func in funcs:
        start_time = time.perf_counter()
        func(arg)
        end_time = time.perf_counter()
        if best_time > end_time - start_time:
            best_time = end_time - start_time
            # print(best_time)
            best_func = func
    return best_func
'''
def slow(arg):
    time.sleep(3)

def fast(arg):
    time.sleep(1)

funcs = [slow, fast]

print(get_the_fastest_func(funcs, 0))
'''

# step 12
'''
from math import factorial                   # функция из модуля math     

def factorial_recurrent(n):                  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)    

def factorial_classic(n):                    # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

funcs = [factorial, factorial_recurrent, factorial_classic]

print(get_the_fastest_func(funcs, 900))
'''

# step 13
'''
def fib_recurrent(n):                                    # рекурсивная функция
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recurrent(n - 1) + fib_recurrent(n - 2)    


def fib_classic(n):                                      # итеративная функция
    f0, f1 = 0, 1
    for _ in range(n):
        f0, f1 = f1, f0 + f1
    return f0

funcs = [fib_recurrent, fib_classic]

print(get_the_fastest_func(funcs, 10))
'''
# step 14
'''
def for_and_append(a):                            # с использованием цикла for и метода append()
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result
        

def list_comprehension(a):                        # с использованием списочного выражения
    iterations = 10_000_000
    return [i + 1 for i in range(iterations)]    

funcs = [for_and_append, list_comprehension]

print(get_the_fastest_func(funcs, 0))
'''
# step 14
'''
def for_and_append(iterable):             # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result
        

def list_comprehension(iterable):         # с использованием списочного выражения
    return [elem for elem in iterable]    
    

def list_function(iterable):              # с использованием встроенной функции list()
    return list(iterable)

funcs = [for_and_append, list_comprehension, list_function]

print(get_the_fastest_func(funcs, range(100_000)))
'''

# step 16
''''''

