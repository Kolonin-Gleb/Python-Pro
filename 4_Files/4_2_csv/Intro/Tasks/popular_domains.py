# step 17 Популярные домены
'''
Постараюсь решить с использованием модуля csv

План выполнения:

Необходимо прочитать весь файл.
(По сути мне нужен только столбец email)
Я могу прочитать файл в таблицу.
Там с помощью срезов по @ легко получить список доменов и проводить рассчёты уже на нём

Произвести рассчёт наиболее используемых доменов.
Это удобно сделать через словарь?

-) Создать файл domain_usage.csv вида:
domain,count
rambler.ru,24

Домены расположить в порядке возрастания пользоватей + по алфавиту

    data = file.read()
    table = [r.split(',') for r in data.splitlines()]

with open('data.csv', encoding='utf-8') as file:
    file.readline() # Пропускаю заголовки
    domens = [r.split('@')[1] for r in file.read().splitlines()] # Получаю из файла только домены

    res_d = {} # ключ - домен, значение - частота
    for domen in domens:
        res_d[domen] = res_d.get(domen, 0) + 1

    sorted_tuples = sorted(res_d.items(), key=lambda tup: (tup[1], tup[0]) ) # Отсортировать словарь по числу + алфавиту
    res_d = dict(sorted_tuples)

    # Запись словаря в файл
    with open('domain_usage.csv', mode='w', encoding='utf-8') as file:
        file.write('domain,count\n')
        for domain, frequency in res_d.items():
            file.write(f"{domain},{frequency}\n")
'''

# step 18 WiFi Москвы
'''
Задача очень похожа на предыдущую.
Теперь разделитель - ;

Из 2 столбца получаю название района
Из 4 кол. точек доступа по адресу. Потом нужно будет суммировать
'''


with open('wifi.csv', encoding='utf-8') as file:
    file.readline() # Пропускаю заголовки
    data = file.read()
    districts = [r.split(';')[1] for r in data.splitlines()]
    access_points = [r.split(';')[3] for r in data.splitlines()]

    res_d = {} # ключ - домен, значение - частота
    for district, access_points in zip(districts, access_points):
        res_d[district] = res_d.get(district, 0) + int(access_points)

    # TODO: Проблема с сортировкой.
    # районы при совпадении количества точек доступа располагаются в обратном лексикографическом порядке.

    # Сортировка по кол. точек доступа
    sorted_tuples = sorted(res_d.items(), key=lambda tup: (tup[1], tup[0])) # Возрастание точек доступа и алфавита

    # Добавляю специальные num, по порядку всем кортежам.
    # Нужно для сортировки районов с одинаковым числом точек.
    # Сортирую по убыванию числа точек и убыванию num.
    districts = []
    for num, tup in enumerate(sorted_tuples, start=1):
        districts.append([*tup, -num])

    # Сортировка по убыванию кол. точек доступа и возрастанию алфавита
    districts = sorted(districts, key=lambda dist: (dist[1], dist[2]), reverse=True)

    for district in districts:
        print(f"{district[0]}: {district[1]}")
    