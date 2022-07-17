# 2 Схожие буквы
'''
eng = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" # 1
rus = "АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя" #0
result = 0

for i in range(3):
    inp = input()
    if inp in eng:
        result += 1
    elif inp in rus:
        result += 0

if result == 3:
    print('en')
elif result == 0:
    print('ru')
else:
    print('mix')
'''

# 4 Более одного
'''
frequency_d = dict()
lst = [int(num) for num in input().split()]

for num in lst:
    frequency_d[num] = frequency_d.get(num, 0) + 1

ans = []

for item in frequency_d.items():
    if item[1] > 1:
        ans.append(item[0])
print(*sorted(ans))
'''

# 5 Максимальная группа
'''
def sum_of_digits_of(numbers):
    result = []
    for num in numbers:
        result.append(0)
        for dig in num:
            result[-1] += int(dig)
    return result

numbers = [str(num) for num in range(1, (int(input()))+1)]
# print(numbers)
# print(sum_of_digits_of(numbers))

# Группировка с помощью словаря
group_nums = {}
# цикл по 2м спискам с 2мя пер
for group, value in zip(sum_of_digits_of(numbers), numbers):
    group_nums[group] = group_nums.get(group, 0) + 1

print(max(group_nums.values()))
'''

# Более элегантное решение
'''
data = {}
for i in range(1, int(input()) + 1):
    sum_of_digis = sum(map(lambda d: int(d), str(i)))
    data[sum_of_digis] = data.get(sum_of_digis, 0) + 1

print(max(data.values()))
'''

# 6 Трудности перевода
# Удобно решить через пересечения множеств!
'''
n = int(input())
# Сохраняю первые языки
lang_set = set(input().split(', '))

for i in range(n - 1):
    lang_set.intersection_update(set(input().split(', ')))
if lang_set:
    print(*sorted(lang_set), sep=', ')
else:
    print("Сериал снять не удастся")
'''

# 7 Схожие слова
'''
Мой план:
1) Определить кол. глассных в этих словах. Оно должно совпадать.
2) Запустить цикл поиска глассных в обоих словах (Ниже прототип)
3) По мере того, как нахожу глассные на одинаковой позиции уменьшаю число оставшихся для поиска глассных.
- Если все глассные найденны, то можно дальше не идти и прервать цикл. Слова схожие.

def get_vovels_count(word):
    total = 0
    for letter in word:
        if letter in 'ауоыиэяюёе':
            total += 1
    return total

vovels = 'ауоыиэяюёе'
similar_words = []

origin_word = input()
n = int(input())

for _ in range(n): # Ввод слов с || определением их похожести
    origin_vovels_count = get_vovels_count(origin_word) # Восстановление числа глассных для обнаружения
    word = input()

    if origin_vovels_count == get_vovels_count(word):
        for letter, origin_letter in zip(word, origin_word):
            if letter in vovels or origin_letter in vovels: # Столкнулся с гласной
                if origin_letter in vovels and letter in vovels:
                    origin_vovels_count -= 1
                    if origin_vovels_count == 0:
                        similar_words.append(word)
                        break

print(*similar_words, sep='\n')
'''

# Более элегантное решение!!!
'''
vowels = ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')
pattern = [i for i, c in enumerate(input()) if c in vowels] # patter - список, что хранит индексы гласных
print(pattern)


for _ in range(int(input())):
    word = input()
    if [i for i, c in enumerate(word) if c in vowels] == pattern:
        print(word)
'''
