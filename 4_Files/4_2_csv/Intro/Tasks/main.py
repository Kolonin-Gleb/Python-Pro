'''
import csv
with open('Tasks\grades.csv', encoding='utf-8') as csv_file:
    # создаем reader объект и указываем в качестве разделителя символ ;
    rows = csv.reader(csv_file, delimiter=';')
    # выводим каждую строку
    for row in rows:
        print(row)
'''

# Скидки
# выводит названия тех товаров, цена на которые уменьшилась. Сохранить исходный порядок
'''

with open('sales.csv', encoding='utf-8') as file:
    data = file.read() # Читаю файл в строковую пер.
    table = [r.split(';') for r in data.splitlines()] # Делю на строки по \n и строки делю на списки по ;
    del table[0] # Удаляю заголовки
    for row in table:
        if int(row[1]) > int(row[2]):
            print(row[0])
# Альтернативный вариант
import csv

with open("sales.csv", encoding="utf-8") as file:
    csv_dict_reader = csv.DictReader(file, delimiter=";")
    for row in csv_dict_reader:
        if int(row["new_price"]) < int(row["old_price"]):
            print(row["name"])
'''

# Сортировка csv по столбцу
# Мне необходимо считать файл в список, чтобы потом удобно сортировать используя индексы
'''
col_num = int(input()) # 1 - str, 2 - int, 3 - int

with open('deniro.csv', encoding='utf-8') as file:
    data = file.read()
    table = [row.split(',') for row in data.splitlines()]
    if col_num == 1:
        table.sort(key=lambda item: item[0])
    elif col_num == 2:
        table.sort(key=lambda item: int(item[1]))
    else:
        table.sort(key=lambda item: int(item[2]))
    for row in table:
        print(*row, sep=',')
'''

# упорядочивает компании по возрастанию средней зарплаты ее сотрудников и выводит их названия,
# каждое на отдельной строке.
# Если две компании имеют одинаковые средние зарплаты,
# они должны быть расположены в алфавитном порядке их названий.
'''
# Средняя ЗП
# Разделитель - ;
# Думаю, что тут лучше сформировать словарь.
# Т.к. взаимодействие с 1ой компанией будет производиться много раз

План:

1) Читаю строку.
Получаю из неё название компании - ключ
Ключу соответсвует список вида [сумма ЗП, кол. ЗП, ср.ЗП] 
Используя такой словарь я смогу провести нужную сортировку?
- Да. Я смогу отсортировать по ЗП и алфавиту исп. специальную lambda

Средняя зарплата компании = суммы всех зарплат / их количество.

import csv
analysis_d = {}

with open('salary_data.csv', encoding='utf-8') as file_csv:
    rows = csv.DictReader(file_csv, fieldnames=['company_name', 'salary'], delimiter=';')

    # Пропускаю строку заголовков. Костыль
    costil = 0 
    for row in rows:
        if costil == 0:
            costil += 1
            continue

        # Формирую ключ - для новой компании и получаю её значения или [0, 0, 0]
        company_stats = analysis_d.get(row['company_name'], [0, 0, 0])
        # Формирую новые значения исходя из имеющихся данных для тек. компании
        analysis_d[row['company_name']] = [company_stats[0] + int(row['salary']), company_stats[1] + 1, 0]

# Из статистики рассчитываю и сохраняю только среднюю ЗП для всех компаний
for company in analysis_d.keys():
    company_stats = analysis_d.get(company) # Текущая статистика компании
    # Обновление статистики по компании
    analysis_d[company] = company_stats[0] / company_stats[1]

# Сортировка 
res = sorted(analysis_d.items(), key=lambda x: (x[1], x[0]))
for company in res:
    print(company[0])

'''

# step 16 csv_columns
'''

def csv_columns(filename: str):
    res_d = {}
    with open(filename, encoding='utf-8') as file:
        data = file.read()
        table = [r.split(',') for r in data.splitlines()]
        columns = table[0]
        del table[0] # Удаляю заголовки
        # Добавляю в словарь ключи - названия столбцов и заготовки для их значений
        for col in columns:
            res_d.setdefault(col, [])
        
        for row in table: # Построчное чтение таблицы
            for ind, key in enumerate(res_d):
                res_d[key].append(row[ind])
    return res_d

print(csv_columns('exam.csv'))
'''

# step 15
# Возрастание классов
'''
План действий.

1 столбец нужно перенести без изменений

Здесь необходимо провести сортировку столбцов, т.е. расставить их в нужном порядке.

Нужно прочитать столбцы в словари, где:
ключ - номер класса
значение - список значений в столбце

Затем произвести сортировку по ключам словаря 
И реализовать постолбчатую запись в файл
'''

import numpy as np
import csv

with open('student_counts.csv', mode='r', encoding='utf-8') as file:
    data = file.read()
    table = [r.split(',') for r in data.splitlines()]

    table = np.array(table)
    table = table.T # Столбцы в виде строк

    # Забираю столбец years
    years_col = list(table[0])
    table = np.delete(table, 0, axis=0)

    res_d = {}
    # Превращаю таблицу в словарь
    for col in table:
        header = col[0].split('-')
        header = int(header[0]), header[1]
        res_d.setdefault(header, col[1:]) # key: (5, 'Б'), values: кол-ва учеников в этом классе

    # Сортировка словаря по ключам-кортежам (числу и букве)
    sorted_tuples = sorted(res_d.items())
    res_d = dict(sorted_tuples)

    # Новый словарь с ключами-заголовками в виде соответствующему отображаемому
    res_d2 = {years_col[0]: years_col[1:]} # Возращаю столбец years в словарь для дальнейшей записи

    for header in res_d.keys():
        new_header = '-'.join((str(header[0]), header[1]))
        res_d2.setdefault(str(new_header), res_d[header])

    # print(res_d2)
    # Остаётся осуществить запись
    # dictWriter может быть полезен!

with open('sorted_student_counts.csv', mode='w', encoding='utf-8') as file_csv:
    writer = csv.DictWriter(file_csv, fieldnames=[list(res_d2.keys())]) # названия всех столбцов

    # RES_D2 - должен быть списком словарей!
    res_d3 = []
    for item in res_d2.items():
        item = list(item)
        res_d3.append({str(item[0]): list(item[1])})

    print(res_d3)
    # writer.writeheader() # Записываю заголовки (названия всех столбцов)
    writer.writerows(res_d3)


# Напишите программу, которая записывает данную таблицу в файл sorted_student_counts.csv, 
# располагая все столбцы в порядке возрастания классов,
# при совпадении классов — в порядке возрастания букв.


