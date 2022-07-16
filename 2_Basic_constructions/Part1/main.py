# 3 hide_card
'''
def hide_card(card_number: str):
    card_number = card_number.replace(' ', '')
    return '************' + card_number[12:]


card = '1234567890123456'
print(hide_card(card))
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
Нужно будет повторить формат аргументов для функций
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
