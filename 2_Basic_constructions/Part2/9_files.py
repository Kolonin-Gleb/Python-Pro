# 9 Файлы в файле
'''
Мой план решения задачи:

1) Открыть файл в режиме чтения и читать его по строчкам +
2) Выполнять split каждой строчки по пробелу +
- Определять расширения файла, считывая симовлы после . до " "
- Добавлять строчку в группу с этим расширением (будет представлена списком)
- Отсортировать группу, чтобы файлы были в алфавитном порядке

3) Перевод всех размеров файлов в наименьшую ед. изм. (B)
- Суммирование ед. изм.
- Постепенный перевод во всё большие ед. изм. по математическому округлению.
- Таким образом определяется итоговый вес всех файлов этой группы

4) Вывод групп по алфавиту

Группы должны быть расположены в алфавитном порядке расширений,
файлы в группах — в алфавитном порядке их имен.
'''

'''
1 KB = 1024 B
1 MB = 1024 KB
1 GB = 1024 MB
'''

def sum_weights(weights):
    total = [0, 'B']
    # Перевод в Байты с суммированием
    for weight in weights:
        if weight[1] == 'B':
            total[0] += int(weight[0])
        elif weight[1] == 'KB':
            total[0] += int(weight[0]) * 1024
        elif weight[1] == 'MB':
            total[0] += int(weight[0]) * 1024 * 1024
        elif weight[1] == 'GB':
            total[0] += int(weight[0]) * 1024 * 1024 * 1024
    # Перевод Байт в большую меру
    if total[0] >= 1024:
        total[0] = round(total[0] / 1024)
        total[1] = 'KB'
    if total[0] >= 1024:
        total[0] = round(total[0] / 1024)
        total[1] = 'MB'
    if total[0] >= 1024:
        total[0] = round(total[0] / 1024)
        total[1] = 'GB'
    return total

extensions_d = dict() # Словарь. Ключ - расширение, Значение - список файлов

with open('files.txt', 'r', encoding='utf-8') as f:
    for line in f: # Чтение всего файла по строкам
        line = line.rstrip()
        ext = line[line.find('.'):line.find(' ')]
        extensions_d.setdefault(ext, []).append(line)

weights = [] # Веса в тек. группе
# Сортировка файлов групп по алфавиту
keys_order = sorted(extensions_d.keys())

for key in keys_order:
    extensions_d[key] = sorted(extensions_d[key])
    for value in extensions_d[key]:
        print(value[:value.find(' ')]) # Вывод файла без веса
        weights.append(value[value.find(' ')+1::].split()) # Сохранение веса файла
    print("----------")
    print("Summary: ", end='')
    print(*sum_weights(weights), end="\n\n")
    weights = [] # Сброс накопленных весов
