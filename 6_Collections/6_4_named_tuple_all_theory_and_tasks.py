# Именованные кортежи

'''
Именнованные кортежи используются для улучшения читаемости кода


'''

# Объявление и создание именнованного кортежа
''' 
from collections import namedtuple

# Объявление типа Point -именнованного кортежа с полями x и y
Point = namedtuple('Point', ['x', 'y']) 

point = Point(3, 7) # Создание именнованного кортежа point

print(point)
print(point.x, point.y) # Получение значений кортежа по именам полей
print(point[0], point[1]) # Получение значений кортежа по индексам полей
print(type(point))
'''
# Кортежи и именнованные кортежи неизменяемы, но могут содержать изменяемые значения
'''
tup = (1, ['one', 'two'])
print(tup)

from collections import namedtuple

Person = namedtuple('Person', ['name', 'children'])
sveta = Person('Sveta Gueva', ['Larisa', 'Timur'])
print(sveta)

sveta.children.append('Soslan')
print(sveta)
'''

# Функция namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
'''
'''

# Хитрая задачка
'''
from collections import namedtuple

Movie = namedtuple(typename='Movie', field_names=['name', 'genres', 'director', 'imdb_rating'])
movie = Movie('La La Land', ['comedy', 'drama', 'musical'], 'Damien Chazelle', 8)

print(movie)
# print(movie['name'])
# print(movie('name'))
print(movie.name)
print(movie[0])
# print(movie[1])
'''

# Атрибуты _fields и _field_defaults
'''
# Типы данных, что возращают аттрибуты
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'height'], defaults=[])

tim = Person('Тимур', 29, 170)

print(tim)
print("_fields")
print(tim._fields)
print(type(tim._fields)) #tuple

print("_field_defaults")
print(tim._field_defaults)
print(type(tim._field_defaults)) #dictionary
'''

# step 10
'''
from collections import namedtuple
import pickle # Для работы с сериализованными данными

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', 'rb') as file:
    animals_lst = pickle.load(file)
    # print(animals_lst)

for animal in animals_lst:
    for field, value in zip(Animal._fields, animal):
        print(f"{field}: {value}")
    print()
'''

# step 11
'''
from collections import namedtuple

User = namedtuple('User', ['name', 'surname', 'email', 'plan'])

users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
         User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
         User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
         User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
         User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
         User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
         User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
         User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
         User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
         User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
         User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
         User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
         User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
         User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
         User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]

# Сортировка:
# отсортировав их по статусу подписки от дорогой к дешевой, 
# а при совпадении статусов — по алфавиту адресов электронных почт

statuses = {
    'Gold': 1,
    'Silver': 2,
    'Bronze': 3,
    'Basic': 4
}

users.sort(key=lambda user: (statuses.get(user.plan), user.email))

for user in users:
    print(user.name, user.surname)
    print(f"  Email: {user.email}")
    print(f"  Plan: {user.plan}")
    print()
'''

# step 12
'''
План выполнения.

Я могу прочитать файл в:
1. Словарь, где ключ - имя столбца, а значение - список его значений.
2. Список именнованных кортежей +
Мне 2 вариант нравится больше, т.к. уже делал аналогичное выше

Как выполнить сортировку по вохрастанию столбцов даты и времени?
- Даты находятся в нестандартном формате. Нужно будет изменять.

from datetime import datetime, time

with open('meetings.csv', 'r', encoding='utf-8') as file:
    guests = []
    file.readline() # Пропускаю заголовки
    data = [line.strip().split(',') for line in file.readlines()] # Читаю файл в таблицу
    data.sort(key=lambda guest: (datetime.strptime(guest[2], '%d.%m.%Y').date(), time().fromisoformat(guest[3]))) # Сортирую
    for guest in data:
        print(f"{guest[0]} {guest[1]}")
'''

# 
''''''