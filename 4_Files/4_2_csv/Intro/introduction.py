# Простая теория
'''
with open('products.csv', encoding='utf-8') as file:
    data = file.read()
    for line in data.splitlines():
        print(line.split(','))

print("=============================================")

# Создание списка-таблицы для взаимодействия с прочитанными данными с исп. индексов 
with open('products.csv', encoding='utf-8') as file:
    data = file.read()
    table = [r.split(',') for r in data.splitlines()]
    print(*table) # Вся таблица
    print(table[7][1]) # Цена 6ого товара (1 строка - заголовки)

print("=============================================")
# Сортировка товаров по цене и вывод 5 самых дешевых

with open('products.csv', encoding='utf-8') as file:
    data = file.read()
    table = [r.split(',') for r in data.splitlines()]
    del table[0] # Удаляю заголовки
    table.sort(key=lambda item: int(item[1]))
    for line in table[:5]:
        print(line)
'''

# Модуль CSV reader - для чтения
'''
import csv
# reader - объект для чтения
with open('products.csv', encoding='utf-8') as file:
    rows = csv.reader(file) # Объект чтения csv (Итератор)
    for row in rows:
        print(row)
'''

# DictReader - Для чтения с удобным обращением по названию столбца к полям
'''
import csv
with open('products2.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';', quotechar='"')
    for row in rows:
        print(dict(row)) # Таким образом csv файл будет представлен в виде словаря


with open('products2.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';', quotechar='"')
    exp_to_cheap = sorted(rows, key=lambda item: int(item['price']), reverse=True)
    for record in exp_to_cheap[:5]:
        print(dict(record))
'''

# writer - для записи данных
'''
import csv

columns = ['first_name', 'second_name', 'class_number', 'class_letter']
data = [['Тимур', 'Гуев', 11, 'А'], ['Руслан', 'Чаниев', 9, 'Б'], ['Артур', 'Харисов', 10, 'В']]

with open('students.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file) # Объект файла, в который будет производиться запись
    writer.writerow(columns) # Запись заголовков
    # Запись данных
    for row in data:
        writer.writerow(row)
'''

# DictWriter - для записи данных
'''

import csv

# Список словарей
data = [{'first_name': 'Тимур', 'second_name': 'Гуев', 'class_number': 11, 'class_letter': 'А'},
        {'first_name': 'Руслан', 'second_name': 'Чаниев', 'class_number': 9, 'class_letter': 'Б'},
        {'first_name': 'Роман', 'second_name': 'Белых', 'class_number': 10, 'class_letter': 'В'}]

columns = ['first_name', 'second_name', 'class_number', 'class_letter']

with open('students2.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=columns, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for row in data:
        writer.writerow(row)
'''

