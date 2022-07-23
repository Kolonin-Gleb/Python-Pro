# import sys

# Потоковый ввод
'''
# Будер работать как эхо
for line in sys.stdin:
    print(line.strip('\n'))

# Работа с потоковым вводом sys.stdin - полезна, когда неизвестен момент остановки ввода данных пользователем 
'''

# Потоковый вывод
'''
print('Hello')
sys.stdout.write('Hello') # Но тут нет переноса строки 
# Этот код равносилен, т.к. print передаёт данные для печати потоковому выводу

# sys.stdout.write(24) # Приведёт к ошибке. В поток вывода можно передавать только СТРОКИ
'''

# tasks

# step 10 Обратный порядок
'''
import sys
data = [line[::-1].strip() for line in sys.stdin]
print(*data, sep='\n')
'''

# step 11 Разница между датами
'''
# Будер работать как эхо
for line in sys.stdin:
    print(line.strip('\n'))
'''

# step 12 Лемма о трёх носках
'''
import sys

players_socks = {'Анри': 0, 'Дима': 0}

for turn, line in enumerate(sys.stdin):
    socks = int(line)

if turn % 2 == 0: #Чётный ход - Анри последний
    if socks % 2 == 0:
        print("Анри")
    else:
        print("Дима")
else: # Нечётный ход - Дима последний
    if socks % 2 == 0:
        print("Дима")
    else:
        print("Анри")
'''
# Более элегантное решение
'''
import sys # Т.к. не знаю, когда прекратится ввод данных

data = [int(x) for x in sys.stdin] # Сохраняю вводимые числа в список
if (len(data)-1) % 2 == 0: #Чётный ход - Анри последний
    print('Анри' if data[-1] % 2 == 0 else 'Дима')
else: # Нечётный ход - Дима последний
    print('Дима' if data[-1] % 2 == 0 else 'Анри')
'''

# step 13 Урок статистики
'''
import sys

heights = [int(x) for x in sys.stdin]

if heights:
    print(f"Рост самого низкого ученика: {min(heights)}")
    print(f"Рост самого высокого ученика: {max(heights)}")
    print(f"Средний рост: {sum(heights) / len(heights)}")
else:
    print("нет учеников")
'''

# step 14 Комментатор
'''
import sys

lines = [line for line in sys.stdin]
clear_comments = 0

for line in lines:
    for letter in line:
        if letter == ' ': continue
        elif letter == '#':
            clear_comments += 1
        else:
            break

print(clear_comments)
'''

# step 15 Без комментариев
# Почему-то не проходит
'''
import sys
code = [line for line in sys.stdin if line.find('#') == -1]
print(*code, sep='', end='')
print()
'''

