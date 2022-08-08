'''
blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2}, 
              {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
              {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3}, 
              {'Comments': 4, 'Shares': 2}, 
              {'Photos': 8, 'Comments': 1, 'Shares': 1}, 
              {'Photos': 3, 'Likes': 19, 'Comments': 3}]

total_likes = 0

for post in blog_posts:
    try:
        total_likes += post['Likes']
    except KeyError:
        total_likes -= 1

print(total_likes)
'''

'''
food = ['chocolate', 'chicken', 'corn', 'sandwich', 'soup', 'potatoes', 'beef', 'lox', 'lemonade']
fifth = []

for x in food:
    try:
        fifth.append(x[4])
    except IndexError:
        fifth.append('_')
print(fifth)

100
i'm number!
10
[1, 99]
1.1
{'math', 'physics'}
'''

'''
import sys

summa = 0
not_numeric = 0

for line in sys.stdin:
    try:
        summa += float(line.strip())
    except ValueError:
        not_numeric += 1


if int(summa) == summa:
    print(int(summa))
else:
    print(float(summa))

print(not_numeric)
'''

'''
Через 2 try-except

import sys
s, counter = 0, 0
for line in sys.stdin:
    try:
        s += int(line)
    except ValueError:
        try:
            s += float(line)
        except ValueError:
            counter += 1
print(s)
print(counter)
'''

'''
months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

try:
    num = int(input())
    print(months[num])
except ValueError:
    print('Введено некорректное значение')
except KeyError:
    print('Введено число из недопустимого диапазона')
'''

'''
try:
    file = open(input(), 'r', encoding='utf-8')
    try:
        print(file.read())
    finally:
        file.close()
except FileNotFoundError:
    print("Файл не найден")
'''
'''
def add_to_list_in_dict(data: dict, key, element):
    try:
        data[key].append(element)
    except KeyError:
        data.setdefault(key, [element])


data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
add_to_list_in_dict(data, 'b', 7)

print(data)

# {'a': [1, 2, 3], 'b': [4, 5, 6, 7]}
'''

'''
week = {
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "Воскресенье",
}

def get_weekday(number: int):
    if type(number) != int:
        raise TypeError("Аргумент не является целым числом")
    elif number < 1 or number > 7:
        raise ValueError("Аргумент не принадлежит требуемому диапазону")
    else:
        return week[number]
    

try:
    print(get_weekday('hello'))
except Exception as err:
    print(err)
    print(type(err))
# Аргумент не является целым числом
# <class 'TypeError'>

try:
    print(get_weekday(8))
except ValueError as err:
    print(err)
    print(type(err))
# Аргумент не принадлежит требуемому диапазону
# <class 'ValueError'>
'''

'''
def get_id(names: list, name: str):
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'

    if type(name) != str:
        raise TypeError('Имя не является строкой')
    else: # Проверка на корректность
        if name[0] in upper_letters:
            for i in range(1, len(name)):
                if name[i] not in lower_letters:
                    raise ValueError('Имя не является корректным')
        else:
            raise ValueError('Имя не является корректным')

    return len(names) + 1
'''
# Более элегантно
'''
def get_id(names, name):
    if type(name) != str:
        raise TypeError('Имя не является строкой')
    if not (name[0].isupper() and name[1:].islower() and name.isalpha()):
        raise ValueError('Имя не является корректным')
    return len(names) + 1

names = ['Timur', 'Anri', 'Dima']
name = 'Arthur'

print(get_id(names, name))
# 4

names = ['Timur', 'Anri', 'Dima', 'Arthur']
name = 'Ruslan1337'
try:
    print(get_id(names, name))
except ValueError as e:
    print(e)
# Имя не является корректным

names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
name = ['E', 'd', 'u', 'a', 'r', 'd']

try:
    print(get_id(names, name))
except TypeError as e:
    print(e)
# Имя не является строкой
'''

# Десериализация JSON
'''
import json

try:
    file = open(input(), 'r', encoding='utf-8')
    try:
        json_data = json.load(file)
        print(json_data)
    except:
        print("Ошибка при десериализации")
    finally:
        file.close()
except FileNotFoundError:
    print("Файл не найден")
'''

'''
import json

try:
    with open(input(), 'r', encoding='utf-8') as file:
        print(json.load(file)) # Попытка напечатать результат десериализации
        
except ValueError:
    print("Ошибка при десериализации")
except FileNotFoundError:
    print("Файл не найден")
'''

# Обработка исключений. Часть 5
'''
# Создание пользовательского исключения

class NegativeAgeError(Exception):
    pass

# Использование пользовательского исключения
try:
    print('Введите свой возраст')
    age = int(input())
    if age < 0:
        raise NegativeAgeError('Возраст не может быть отрицательным')
    print('Ваш возраст равен', age)
except ValueError:
    print('Возраст должен быть числом')
except NegativeAgeError as e:
    print(e)
'''
# is_good_password()
# в стиле LBYL
'''
def is_good_password(string: str):
    if len(string) >= 9:
        if string not in (string.upper(), string.lower()):
            for letter in string:
                if letter.isdigit():
                    return True
    return False

print(is_good_password('41157082'))
# False

print(is_good_password('мойпарольсамыйлучший'))
# False

print(is_good_password('МойПарольСамыйЛучший111'))
# True
'''

# is_good_password()
# В стиле EAFP
'''
# Пользовательские ошибки
class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

def is_good_password(string: str):
    if len(string) < 9:
        raise LengthError
    elif string in (string.upper(), string.lower()):
        raise LetterError
    else:
        for letter in string:
            if letter.isdigit():
                return True
        raise DigitError


try:
    print(is_good_password('Short7'))
except Exception as err:
    print(type(err))
# <class '__main__.LengthError'>

print(is_good_password('еПQSНгиfУЙ70qE'))
# True

try:
    print(is_good_password('41157081231232'))
except Exception as err:
    print(type(err))
# <class '__main__.LetterError'>

try:
    print(is_good_password('4abcdABC8'))
except Exception as err:
    print(type(err))
'''

# Уж лучше матрицы 
'''
class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

def is_good_password(string: str):
    try:
        if len(string) < 9:
            raise LengthError("LengthError")
        elif string in (string.upper(), string.lower()):
            raise LetterError("LetterError")
        else:
            for letter in string:
                if letter.isdigit():
                    return "Success!"
            raise DigitError("DigitError")
    except PasswordError as e:
        print(e)

while True:
    if is_good_password(input()) == "Success!":
        print("Success!")
        break
'''

# Оператор assert
'''
file1 = 'city.jpeg'
file2 = 'data.txt'

assert file1.endswith('.jpeg') or file2.endswith('.jpeg')
'''
