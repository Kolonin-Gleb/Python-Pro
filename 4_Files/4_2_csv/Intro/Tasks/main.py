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
'''

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

