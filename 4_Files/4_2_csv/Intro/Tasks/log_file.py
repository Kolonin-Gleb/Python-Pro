# Бета
'''
Цель и план решения:
Прочитать файл.
Выбрать для каждого email запись с последней датой
- Файл можно прочитать в словарь, где:
ключ = email
значение = список кортежей, где (имя, дата изменения). 
Этот кортежи для списка нужно будет сформировать выбирая записи с тем же email

Записать выбранные записи в новый файл в алфавитном порядке имён
'''
# Мой вариант решения
'''
Прочитать файл в таблицу.
Сделать сортировку по убыванию email и убыванию даты
- Сохраняю первую запись с этим email.
- Пропускаю все следующие записи с этим email

'''

from datetime import datetime

dt_pattern = '%d/%m/%Y %H:%M'

headers = ''
data = []

with open(r'Intro\name_log.csv', 'r', encoding='utf-8') as file:
    headers = file.readline()
    data = [line.strip().split(',') for line in file.readlines()]
    # Сортировка по email и datetime, чтобы получить последние имена для каждого email
    data.sort(key= lambda line: (line[1], datetime.strptime(line[2], dt_pattern)), reverse=True)

with open('new_name_log.csv', 'w', encoding='utf-8') as file:
    newest_data = []
    file.write(headers)
    last_added_email = ''
    for line in data:
        if last_added_email != line[1]:
            newest_data.append(line)
            last_added_email = line[1]

    for line in sorted(newest_data, key= lambda line: line[1]):
        print(*line, sep=',', file=file)
'''
angry-barbara2,barbaraanderson@bk.ru,17/11/2021 01:17
dead-barbara6,barbarabrown@rambler.ru,27/11/2021 08:27
busy_barbara7,barbaradavis@aol.com,24/11/2021 08:24
'''
