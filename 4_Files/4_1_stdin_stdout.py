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
''''''

# step 12 
'''
# Будер работать как эхо
for line in sys.stdin:
    print(line.strip('\n'))
'''

# step 13 Лемма о трёх носках
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

# step 
''''''

