# Декораторы

# Создание декотратора без специального синтаксиса
'''
def sample_decorator(func): # Декоратор, для любой передаваемой функции
    def wrapper():
        print('Начало функции')
        func()
        print('Конец функции')
    return wrapper

def say():
    print('Привет Мир!')

say = sample_decorator(say) # декорирование функции. Применение декоратора
say() # вызов декорированной функции
'''

# Создание декоратора с использованием спец. синтаксиса
# В таком случае функция декорируется при инициализации, и пропадает возможность вызова недекоррированного варианта.
'''
def sample_decorator(func):
    def wrapper(): # Логика декоратора
        print("Начало функции")
        func()
        print("Конец функции")
    return wrapper

@sample_decorator # Применение декоратора
def say():
    print("Hello world!")

say()
'''

# Применение нескольких декораторов
# 1) Декораторы применяются снизу вверх
# 2) Ручное применение нескольких декораторов greet = bold(italic(greet))
# Декорирование функций, принимающих аргументы
'''
def bold(func):
    def wrapper(*args, **kwargs):
        return '<b>' + func(*args, **kwargs) + '</b>'
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        return '<i>' + func(*args, **kwargs) + '</i>'
    return wrapper


@bold
@italic
def greet():
    return "Hello world!"

@bold
def greetPerson(name: str):
    return f"Hello, {name}!"


print(greet())
print(greetPerson("Gleb"))
'''

# Возврат значений из декорируемой функции
# Необходимо использовать return в wrapper
'''
def talk(func):
    def wrappper(*args, **kwargs):
        dash = '-' * 15
        result = func(*args, **kwargs)
        return dash + '\n' + result + '\n' + dash
    return wrappper

@talk
def greet(name):
    return f'Hello, {name}'

print(greet("Gleb"))
'''

# Задачки. Декоратор sandwich
'''
def sandwich(func):
    def wrapper(*args, **kwargs):
        print("---- Верхний ломтик хлеба ----")
        result = func(*args, **kwargs)
        print("---- Нижний ломтик хлеба ----")
        return result
    return wrapper
'''

# Новый print
'''
def upper(func):
    def wrapper(*args, sep=" ", end='\n'):
        args = [str(arg).upper() for arg in args]
        return func(*args, sep=sep.upper(), end=end.upper())
    return wrapper

print = upper(print) # Переопределение функции
'''

# Декоратор do_twice вызывающий декорируемую функцию два раза.
'''
def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper
'''

# Декоратор reverse_args
'''
def reverse_args(func):
    def wrapper(*args, **kwargs):
        args = args[::-1]
        return func(*args, **kwargs)
    return wrapper
'''

# Декоратор exception_decorator
'''
def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs), 'Функция выполнилась без ошибок')
        except:
            return ((None, 'При вызове функции произошла ошибка'))
    return wrapper
'''

# Декоратор takes_positive
'''
def takes_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if type(arg) != int:
                return TypeError
            if arg <= 0:
                return ValueError

        for kwarg in kwargs.values():
            if type(kwarg) != int:
                return TypeError
            if kwarg <= 0:
                return ValueError

        return func(*args, **kwargs)
    return wrapper
'''

