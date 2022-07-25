# import pickle
'''
Модуль pickle используется для бинарной сериализации, т.е. 
сериализации в байты.

.pkl - расширение файла, содержащего бинарно сериализованные объекты

ВАЖНО: pickle сериализация работает только в Python.
С другими языками сериализацию нужно делать в JSON

JSON - сериализация в текстовый формат.
pickle - сериализация в бинарный формат.

pickle быстрее JSON, но менее безопасен
'''

# obj = {'Python': 1991, 'Java': 1995, 'C#':2002}

# Функция dump() - Сериализация объекта в файл
# with open('file.pkl', 'wb') as file:
    # pickle.dump(obj, file)

# Функция load() - Десериализация файла в Python объект
# with open('file.pkl', 'rb') as file:
    # obj = pickle.load(file)
    # print(obj)
    # print(type(obj))

# Функция dumps() - возврат сериализованных данных (байтовая строка)
'''
binary_obj = pickle.dumps(obj)
print(binary_obj)
print(type(binary_obj))
'''

# Функция loads() - десериализация данных из байтовой строки
'''
binary_obj = pickle.dumps(obj)
new_obj = pickle.loads(binary_obj)
print(new_obj)
print(type(new_obj))
'''

# TASKS

# Одинокая функция
'''
import pickle # Для работы с сериализацией
import sys # Для стандартного потока ввода, т.к. неизвестно когда ввод остановится

def func(*args):
    return ' '.join(args)

filename = input() #func.pkl

with open(filename, 'rb') as file:
    f = pickle.load(file) # Десериализация функции
    args = [arg.strip() for arg in sys.stdin] # Для прекращения ввода: Ctrl + Z
    print(f(*args))
'''

# Ты не пройдёшь!
'''
import pickle # Для работы с сериализацией

def filter_dump(filename:str, objects:list, typename: type):
    with open(filename, 'wb') as file:
        # Создаю lst для сериализации
        lst = [obj for obj in objects if type(obj) == typename]
        pickle.dump(lst, file)

filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)
# должен создавать файл numbers.pkl, содержащий сериализованный список [1, 3, 4].
'''

# Контрольная сумма
'''
План выполнения:

Файлы для тестов проги:
1) Создать файл dict.pkl
- сериализовать туда словарь
2) Создать файл list.pkl
- сериализовать туда список
'''
# import pickle
# Создание данных для теста
'''
with open('dict.pkl', 'wb') as file:
    d = {'a': 1, 1: 10, 'b': 2, 2: 20} # Конт. сумма = 3
    pickle.dump(d, file)

with open('list.pkl', 'wb') as file:
    lst = ['a', 'b', 3, 4, 'f', 'g', 7, 8] # Конт. сумма = min() * max() = 24
    pickle.dump(lst, file)
'''

'''
Если список (словарь) не содержит
целочисленных элементов (ключей),
то его контрольная сумма = 0.
'''

# Сама программа
'''
1) Открыть полученный файл
2) Десериализировать его данные
3) Определить словарь или список
4) Вычислить контр. сумму для полученного файла.
Базируясь на том словарь или список
5) Выполнить сравнение
6) Дать ответ
'''
# Решение
'''
import pickle

filename = input()
control_sum = int(input())

with open(filename, 'rb') as file:
    obj = pickle.load(file)
    res_control_sum = 0
    if type(obj) == list:
        # Получить мин и макс. ЦЕЛЫЕ числа из списка python
        nums = [int(x) for x in obj if str(x).isnumeric()]
        if len(nums) == 0:
            res_control_sum = 0
        else:
            res_control_sum = min(nums) * max(nums)
    elif type(obj) == dict:
        for key in obj.keys():
            if type(key) == int:
                res_control_sum += key
    else:
        print("Нераспознанный объект!")

    # print(res_control_sum) # Для наглядности теста
    if control_sum == res_control_sum:
        print("Контрольные суммы совпадают")
    else:
        print("Контрольные суммы не совпадают")
'''
# Более элегантное и точное решение через isinstance()
'''
import pickle

filename, control_sum = input(), int(input())

with open(filename, 'rb') as file:
    obj = pickle.load(file)
    res_control_sum = 0
    if isinstance(obj, list):
        nums = [num for num in obj if isinstance(num, int)] # Получаю только числа
        if nums: # Если не пустой список
            res_control_sum = min(nums) * max(nums)
    elif isinstance(obj, dict):
        nums = [num for num in obj if isinstance(num, int)]
        if nums: # Если не пустой словарь
            res_control_sum = sum(nums)
    # else:
    #     print("Нераспознанный объект!")

    # print(res_control_sum) # Для наглядности теста
    if control_sum == res_control_sum:
        print("Контрольные суммы совпадают")
    else:
        print("Контрольные суммы не совпадают")
'''

