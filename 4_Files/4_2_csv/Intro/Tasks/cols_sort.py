# step 15
# Возрастание классов

import numpy as np

with open('student_counts.csv', mode='r', encoding='utf-8') as file:
    data = file.read()
    table = [r.split(',') for r in data.splitlines()]

    table = np.array(table)
    table = table.T # Столбцы в виде строк

    # Забираю столбец years
    years_col = list(table[0])
    table = np.delete(table, 0, axis=0)

    # Новая таблица для осуществления сортировки
    table2 = []
    for col in table:
        header = col[0].split('-')
        header = [int(header[0]), header[1]]
        table2.append(header)
        table2[-1].extend(col[1:])

    # Сортировка столбцов по названию их столбцов (числу и букве)
    table2.sort(key=lambda lst: (lst[0], lst[1]))
    # print(table2)

    table3 = np.array(table2)
    table3 = table3.T

    # Добавляю по оси столбец с годами

    # Приведение 2 эл. каждого столбца в строку формата '1-А', явл. заголовком
    # 1 эл. послужит для информации о годе, что при последующем транспонировании позволит записать данные в нужном виде
    '''
    for row, year in zip(table2, years_col):
        print(row)
        print(year)
        row[1] = '-'.join((str(row[0]), row[1]))
        row[0] = year

    # TODO: Несколько (11) классов не получили данные! Нарушаются размерности!
    '''

    for row in table2:
        row[1] = '-'.join((str(row[0]), row[1]))
    
    print(len(table2))
    print(len(years_col))
    # for row in table2:
    #     row
        

    print(table2)

    # table3 = np.array(table2)
    # table3 = table3.T
    # print(table3)

    # Остаётся сохранить NumPy в CSV
    # np.savetxt('sorted_student_counts.csv', table3, delimiter=",")


# Напишите программу, которая записывает данную таблицу в файл sorted_student_counts.csv, 
# располагая все столбцы в порядке возрастания классов,
# при совпадении классов — в порядке возрастания букв.
