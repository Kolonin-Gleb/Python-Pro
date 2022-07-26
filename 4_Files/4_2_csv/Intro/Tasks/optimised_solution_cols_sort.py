import numpy as np
import pandas as pd

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

    table2.sort(key=lambda lst: (lst[0], lst[1])) # Сортировка столбцов по названию их столбцов (числу и букве)

    # Восстановление оригинальных заголовков формат '1-А'
    for row in table2:
        row[1] = '-'.join((str(row[0]), row[1]))
        del row[0]

    table2.insert(0, years_col) # Возврат данных о годах

    # Итоговый вид таблицы
    table3 = np.array(table2)
    table3 = table3.T
    # Сохранение NumPy массива в DataFrame с последующей записью в файл
    DF = pd.DataFrame(table3)
    DF.to_csv("sorted_student_counts.csv", index=False, header=None)


# Напишите программу, которая записывает данную таблицу в файл sorted_student_counts.csv, 
# располагая все столбцы в порядке возрастания классов,
# при совпадении классов — в порядке возрастания букв.
