'''
import time
def teleprint(*args, delay=0.05, str_join=' '):
    text = str_join.join(str(x) for x in args)
    n = len(text)
    for i, char in enumerate(text, 1):
        if i == n:
            char = f'{char}\n'
        print(char, end='')
        time.sleep(delay)
        
teleprint('Привет Python!', 'Меня зовут Тимур', 'Beegeek = <3', str_join='*')
teleprint('Привет Python!', 'Меня зовут Тимур', 'Beegeek = <3', str_join='*')
'''

def make_upper(func):
    def wrapper():
        return func().upper()
    return wrapper

def del_first_char(func):
    def wrapper():
        return func()[1:]
    return wrapper

def reverse(func):
    def wrapper():
        return func()[::-1]
    return wrapper

@reverse
@del_first_char
@make_upper
def beegeek():
    return 'beegeek'

print(beegeek())