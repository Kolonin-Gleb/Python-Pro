# Тип данных Counter - используется для подсчёта
'''
from collections import Counter

counter1 = Counter('mississipi') # Счётчик на основе строки
counter2 = Counter(i=4, s=4, p=2, m=1)

print(counter1)
print(counter2)

# Ещё интересный пример

counter2 = Counter(i=5, s='5')
counter1 = Counter(i=4, s='4')

counter2.update(counter1)

print(counter2)
'''

'''
from collections import Counter
pets = Counter(cat=3, dog=3, fox=2, hamster=1)

print(pets['elephant'])
print(*pets)

# Ещё интересный пример

letters = Counter(set('Beautiful is better than ugly'))
print(letters['t'])

# Ещё интересный пример

vegetables = Counter({'cabbage': 10, 'pepper': 7, 'pumpkin': 4})
vegetables.update(['pepper', 'pepper', 'pepper'])
print(vegetables['pepper'])

# Ещё интересный пример


from collections import Counter
clothes = Counter([('shirt', 3), ('dress', 1), ('shirt', 3)])
print(clothes['shirt'])
print(clothes[('shirt', 3)])
'''

# Подсчёт файлов разных типов
'''
from collections import Counter

files = ['emoji_smile.jpeg', 'city-of-the-sun.mp3', 'dhook_hw.json', 'sample.xml',
         'teamspeak3.exe', 'project_module3.py', 'math_lesson3.mp4', 'old_memories.mp4',
         'spiritfarer.exe', 'backups.json', 'python_for_beg1.mp4', 'emoji_angry.jpeg',
         'exam_results.csv', 'project_main.py', 'classes.csv', 'plants.xml',
         'cant-help-myself.mp3', 'microsoft_edge.exe', 'steam.exe', 'math_lesson4.mp4',
         'city.jpeg', 'bad-disease.mp3', 'beauty.jpeg', 'hollow_knight_silksong.exe',
         'whatsapp.exe', 'photoshop.exe', 'telegram.exe', 'yandex_browser.exe',
         'math_lesson7.mp4', 'students.csv', 'emojis.zip', '7z.zip',
         'bones.mp3', 'python3.zip', 'dhook_lsns.json', 'carl_backups.json',
         'forest.jpeg', 'python_for_pro8.mp4', 'yandexdisc.exe', 'but-you.mp3',
         'project_module1.py', 'nothing.xml', 'flowers.jpeg', 'grades.csv',
         'nvidia_gf.exe', 'small_txt.zip', 'project_module2.py', 'tab.csv',
         'note.xml', 'sony_vegas11.exe', 'friends.jpeg', 'data.pkl']

# Расширения должны быть расположены по алфавиту, каждый на отдельной строке, в следующем формате:
# <расширение>: <количество файлов>

# Выполнение подсчётов
extensions_counter = Counter([extension[extension.find('.')+1:] for extension in files])

# Вывод формата ключ: значение
for extension in sorted(extensions_counter):
    print(f"{extension}: {extensions_counter[extension]}")
'''

# Функция count_occurences()
'''
from collections import Counter

# Функция должна определять, сколько раз слово word встречается в последовательности words, и возвращать полученный результат.
def count_occurences(word: str, words: str):
    word_counter = Counter([word.lower() for word in words.split()])
    return word_counter[word.lower()]


word = 'Java'
words = 'Python C++ C# JavaScript Go Assembler'

print(count_occurences(word, words))
'''

# Не поленимся и запишем
'''
from collections import Counter

purchases_counter = Counter(input().split(','))

# Товары должны быть расположены в лексикографическом порядке, каждый на отдельной строке, в следующем формате:
for purchase in sorted(purchases_counter):
    print(f"{purchase}: {purchases_counter[purchase]}")
'''

# А сколько стоит курс
'''
<товар>: <цена за единицу товара> UC x <количество товаров в группе> = <общая стоимость группы> UC
Примечание 1. Программа должна добавлять нужное количество пробелов, если название товара имеет меньшую длину, чем другие.

Примечание 2. Получить Unicode код символа можно с помощью функции ord().
'''

'''
from collections import Counter

def get_price(purchase: str):
    return sum([ord(letter) for letter in purchase if letter != ' '])

purchases_counter = Counter(input().split(','))

max_length_purchase = len(max(purchases_counter.keys(), key=len))

for purchase in sorted(purchases_counter):
    # Довести длину purchase до max_length_purchase пробелами
    purchase_print = purchase
    if len(purchase_print) != max_length_purchase:
        purchase_print += ' ' * int(max_length_purchase - len(purchase_print))

    print(f"{purchase_print}: {get_price(purchase)} UC x {purchases_counter[purchase]} = {purchases_counter[purchase] * get_price(purchase)} UC")
'''

# Более элегантное решение через ljsut для выравнивания
'''

from collections import Counter

def get_price(product):
    return sum(map(ord, filter(str.isalpha, product)))

products = Counter(input().split(','))
pattern = '{}: {} UC x {} = {} UC'
spaces = max(map(len, products))

for product, count in sorted(products.items()):
    price = get_price(product)
    total = price * count
    product = product.ljust(spaces, ' ') # Дополнение пробелами, чтобы выровнять по левому краю согласно длине максимальной покупки
    print(pattern.format(product, price, count, total))

'''

# The Zen of Python
'''
План:

сколько раз встречается каждая буква в этом тексте.
Буквы и их количество должны выводиться по алфавиту, каждая на отдельной строке, в следующем формате:

Программа не должна учитывать регистр, то есть, например, буквы a и A считаются одинаковыми.

Программа должна игнорировать все небуквенные символы.

pythonzen.txt

'''
'''
from collections import Counter

with open('pythonzen.txt', 'r', encoding='utf-8') as file:
    letters_counter = Counter()
    
    for letter in file.read().lower():
        if letter in "abcdefghijklmnopqrstuvwxyz":
            letters_counter[letter] += 1

    # Форматированный вывод:
    for letter in sorted(letters_counter):
        print(f"{letter}: {letters_counter[letter]}")
'''

# Тип данных Counter - часть 2
'''
from collections import Counter

counter1 = Counter('abcde')
counter2 = Counter('abcdf')

print(counter1 > counter2)
print(counter1 < counter2)
print(counter1 == counter2)

from collections import Counter

letters1 = Counter('stepik')
letters2 = {'s': 1, 't': 1, 'e': 1, 'p': 1, 'i': 1, 'k': 1}

print(letters1 + letters2)
'''

# В поисках слов 2
'''

from collections import Counter

words = [word.lower() for word in input().split()]
rarest_quantity = Counter(words).most_common()[-1][1]
rare_words = [word[0] for word in Counter(words).most_common()[::-1] if word[1] == rarest_quantity]

print(*sorted(rare_words), sep=', ')
'''

# В поисках слов 3
'''
from collections import Counter

words = [word.lower() for word in input().split()]
biggest_quantity = Counter(words).most_common()[0][1]
common_words = [word[0] for word in Counter(words).most_common() if word[1] == biggest_quantity]

print(max(common_words))
'''

# Статистика длин слов
'''
from collections import Counter

# words = [len(word) for word in input().split()]
stats = Counter([len(word) for word in input().split()])
pattern = 'Слов длины {}: {}'

for key, value in sorted(stats.items(), key=lambda x: x[1]):
    print(pattern.format(key, value))
'''

# Всё ещё достоин
'''
'''

