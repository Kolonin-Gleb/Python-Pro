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
'''

