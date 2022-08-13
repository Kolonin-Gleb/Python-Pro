# Встроенные функции


'''
# собенностью функции round() является то, что округление происходит 
# не по математическим правилам, а до ближайшего четного.
print(round(3.5)) # 4
print(round(4.5)) # 4
print(round(1.65, 1)) # 1.6
print(round(1.55, 1)) # 1.6
print(round(2.7)) # 3 (округление всё равно происходит)
'''

# Строчный алфавит
'''
a-z на каждой строке
ord() и chr()
for i in range(ord('a'), ord('z')+1):
    print(chr(i))
'''

# convert = Почему-то не работает
'''
def convert(num):
    if num == 0:
        return ('0', '0', '0')
    if num > 0:
        return (bin(num)[2:], oct(num)[2:], hex(num)[2:].upper())
    return tuple(f"-{bin(num)[3:]} -{oct(num)[3:]} -{hex(num)[3:]}".upper().split())

print(convert(15))
# ('1111', '17', 'F')
print(convert(-24))
# ('-11000', '-30', '-18')
print(convert(0))
'''

# Фильм с наименьшей средней оценкой
'''
films = {'Spider-Man: No Way Home': {'imdb': 8.8, 'kinopoisk': 8.3},
         'Don"t Look Up': {'imdb': 7.3, 'kinopoisk': 7.6},
         'Encanto': {'imdb': 7.3, 'kinopoisk': 7.4},
         'The Witcher': {'imdb': 8.2, 'kinopoisk': 7.3},
         'Ghostbusters: Afterlife': {'imdb': 7.3, 'kinopoisk': 8},
         'Harry Potter 20th Anniversary: Return to Hogwarts': {'imdb': 8.1, 'kinopoisk': 8.2},
         'Shingeki no Kyojin': {'imdb': 9.0, 'kinopoisk': 8.3},
         'The Matrix': {'imdb': 8.7, 'kinopoisk': 8.5},
         'The Dark Knight': {'imdb': 9.0, 'kinopoisk': 8.5},
         'The Shawshank Redemption': {'imdb': 9.3, 'kinopoisk': 9.1},
         'Avengers: Endgame': {'imdb': 8.4, 'kinopoisk': 7.7}}

# Т.к. делитель всегда одинаковый нет необходимости вычислять среднюю
result = min(films, key=lambda x: sum(films[x].values()))
print(result)
'''

# Функция non_negative_even()
'''
# True, если все числа в списке numbers являются четными и неотрицательными, или False в противном случае.
# Примечание 1. В задаче удобно воспользоваться функцией all().

def non_negative_even(numbers):
    if all(map(lambda num: num >= 0 and num % 2 == 0, numbers)):
        return True
    return False

print(non_negative_even([0, 2, 4, 8, 16]))
# True
print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))
# False
'''

# Проверка
'''
В задаче удобно воспользоваться функцией any().
Функция должна возвращать True, если хотя бы в одном вложенном списке 
сумма всех элементов больше number, и False в противном случае.

def is_greater(lists: list, number: int):
    if any(map(lambda lst: sum(lst) > number, lists)):
        return True
    return False


data = [[-3, 4, 0, 1], [1, 1, -4], [0, 0], [9, 3]]
print(is_greater(data, 10))
# True

data = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
print(is_greater(data, 2))
# False
'''


# Индекс максимального числа
'''
numbers = [-7724, 5023, 3197, -102, -4129, -880, 5857, -2866, -8913, 1195, 9809, 5347, -8071, 903, 3030, -4347, -3354, 1024, 8670, 4210, -5228, 8900, 4823, -2002, 4900, 9520, -3658, 1104, -9554, 3064, 9632, -8701, 3384, 4370, 2034, 7822, -9694, 3347, 7440, -8459, 3238, -5193, -3381, 5281, 9022, 5559, 7593, -6540, -6204, -2483, 8729, 5810, -8254, -9846, -1801, 4882, 3838, -3140, 7609, -3325, 6026, 2994, -1677, 1266, -1893, -4408, -5722, -2841, 9812, 5837, -7474, 4624, -664, 6998, 7888, -971, 8810, 3812, -5396, 2593, 512, -4634, 9735, -3062, 9031, -9300, 3657, 6332, 7552, 8125, -725, 4392, 1727, 8194, -2828, -4314, -8967, -7912, -1363, -5957]
print(numbers.index(max(numbers)))
'''

# my_pow()
'''
def my_pow(number):
    number = str(number)
    summa = 0
    for pos, val in enumerate(number, 1):
        summa += pow(int(val), pos)

    return summa

print(my_pow(139))
# 739
print(my_pow(123))
# 32
'''

# custom_isinstance()
'''
Функция должна возвращать единственное число — количество объектов из списка objects,
которые принадлежат типу typeinfo или одному из типов, если был передан кортеж.

def custom_isinstance(objects: list, typeinfo):
    typeinfo = repr(typeinfo)
    ans = 0
    
    for obj in objects:
        if str(type(obj)) in typeinfo:
            ans += 1
    return ans

numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, int))
# 2

numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, (int, float)))
# 4
'''

# Наиболее успешные сборы
'''
Мультфильмы должны быть расположены в лексикографическом порядке, каждый на отдельной строке, в следующем формате:
<фильм>: <прибыль>$

# Несколько исказил данные для теста сортировки
names = ['Moana', 'Moana', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
budgets = [1, 2, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
box_offices = [2, 1, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]

films_info = list(zip(names, budgets, box_offices))
films_info.sort(key= lambda tup: tup[0])
# Как сработает сортировка, в случае, если первое значение совпадает?
# Будет сохранён исходный порядок. Следующие значения в кортеже не учитываются
for film in films_info:
    print(f"{film[0]}: {film[2]-film[1]}$")
'''

# Функция zip_longest()
# Небольшой читинг)
'''
import itertools

# Переменное кол. аргументов + Арг. fill по умолч. с значением None
def zip_longest(*args, fill=None):
    return list(itertools.zip_longest(*args, fillvalue = fill))


print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, '_'), (5, '_')]

data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
print(zip_longest(*data))
# [(1, 'one', 'I'), (2, 'two', 'II'), (3, 'three', None), (4, None, None), (5, None, None)]
'''

# Необычная сортировка
'''
s = input()

lower_letters = []
upper_letters = []
even_digits = []
odd_digits = []

for letter in s:
    if letter.islower():
        lower_letters.append(letter)
    elif letter.isupper():
        upper_letters.append(letter)
    else:
        if int(letter) % 2 == 0:
            even_digits.append(letter)
        else:
            odd_digits.append(letter)

lower_letters.sort()
upper_letters.sort()
odd_digits.sort()
even_digits.sort()

res = ''
res += ''.join(lower_letters)
res += ''.join(upper_letters)
res += ''.join(odd_digits)
res += ''.join(even_digits)
print(res)
'''

