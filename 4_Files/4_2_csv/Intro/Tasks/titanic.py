with open('titanic.csv', encoding='utf-8') as file:
    file.readline() # Пропускаю заголовки
    data = file.read()
    young_male_survivors = []
    young_female_survivors = []
    for r in data.splitlines():
        r = r.split(';')
        if int(r[0]) == 1 and float(r[-1]) < 18:
            if r[-2] == 'male':
                young_male_survivors.append(r[1])
            else:
                young_female_survivors.append(r[1])

    print(*young_male_survivors, sep='\n')
    print(*young_female_survivors, sep='\n')
