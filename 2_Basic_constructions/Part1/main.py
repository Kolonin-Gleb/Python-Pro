# 3 hide_card
'''
def hide_card(card_number: str):
    card_number = card_number.replace(' ', '')
    return '************' + card_number[12:]


card = '1234567890123456'
print(hide_card(card))
'''

# 4 same_parity
'''
def same_parity(numbers: list):
    if numbers:
        lst = []
        parity = numbers[0] % 2 # Определение чётности/нечётности

        for num in numbers:
            if num % 2 == parity:
                lst.append(num)
        return lst
    return []
# print(same_parity([6, 0, 67, -7, 10, -20]))

# Более элегантное решение
def same_parity(nums: list):
    return [i for i in nums if i % 2 == nums[0] % 2]
'''

# 5 is_valid
'''
def is_valid(pin: str):
    if len(pin) >=4 and len(pin) <= 6 and pin.isnumeric():
        return True
    return False
'''

# 6 print_given
'''
def print_given(*args, **kwargs):
    for ar in args:
        print(ar, type(ar))
    # Вывод именнованных аргументов в алфавитном порядке
    lst = []
    for key, value in kwargs.items():
        lst.append([key, value, type(value)])
    lst.sort(key=lambda sublst: sublst[0])
    for sublst in lst:
        print(*sublst)

# Более элегантное решение
def print_given(*args, **kwargs):
    for arg in args:
        print(arg, type(arg))
    for name, value in sorted(kwargs.items()):
        print(name, value, type(value))
'''

# 7 convert
'''
def convert(user_str: str):
    up, low = 0, 0
    for el in user_str:
        if el.isalpha():
            if el.isupper():
                up += 1
            else:
                low += 1

    if low >= up:
        return user_str.lower()
    else:
        return user_str.upper()

print(convert('pi31415!'))
'''

# 8 filter_anagrams
'''
def filter_anagrams(word: str, words: list):
    # Для проверки на анаграмму отсортирую слова по алфавиту и сравню их ==
    word = ''.join(sorted(word))
    anagrams = []
    for w in words:
        if word == ''.join(sorted(w)):
            anagrams.append(w)
    return anagrams

word = 'abba'
anagrams = ['aabb', 'abcd', 'bbaa', 'dada']

print(filter_anagrams(word, anagrams))
'''

# 9 likes
'''
def likes(names: list):
    if len(names) == 0:
        return "Никто не оценил данную запись"
    elif len(names) == 1:
        return f"{names[0]} оценил(а) данную запись"
    elif len(names) == 2:
        return f"{names[0]} и {names[1]} оценили данную запись"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} и {names[2]} оценили данную запись"
    else:
        return f"{names[0]}, {names[1]} и {len(names) - 2} других оценили данную запись"
'''

# 10 index_of_nearest
'''
# Нужно получить индекс числа максимально близкого к number
# Для этого определю расстояние от каждого эл. до number используя 
# массив модулей разностей элементов входного массива с переданным числом.

def index_of_nearest(numbers :list, number :int):
    if len(numbers) == 0:
        return -1

    distances = []
    for num in numbers:
        distances.append(abs(number - num))
    return distances.index(min(distances))

# print(index_of_nearest([9, 5, 3, 2, 11], 4))
'''

# 11 spell - с произвольным числом аргументов. По умолчанию они - кортеж

# 1) Приведу все слова в нижний регистр 
# 2) Буду идти по словам и создавать ключи словаря из 1ых букв.
# Ставя им в значение длину текущего слова.
# Если слово на эту букву уже имеется, то сохранить длину большего слова
# 3) Вернуть словарь

'''
def spell(*args):
    words = [word.lower() for word in args]
    d = dict()

    for word in words:
        if d.get(word[0], len(word)) <= len(word):
            d[word[0]] = len(word)
    return d

# print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))
'''

# 13 get_biggest
'''
def get_biggest(numbers: list):
    if len(numbers) == 0:
        return -1
    # Сортирую список по убыванию 1ых цифр в числах
    # Соединяюю список в строку и перевожу её в int

    numbers.sort(key=lambda num: str(num)[::], reverse=True)
    numbers = [str(num) for num in numbers]
    biggest = ''.join(numbers)
    return int(biggest)

print(get_biggest([7, 71, 72]))

# в пятом тесте получается 0000... незначащие нули надо убирать.
'''


# Хочу в этой части решить ещё step 4 и step 6. Потом перейду к следующей части