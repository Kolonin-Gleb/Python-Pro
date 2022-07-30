# тип данных ChainMap
'''
Тип данных ChainMap - представляет собой объединение
нескольких словарей.

from collections import ChainMap

empty_chain_map = ChainMap() # Пустой ChainMap
print(empty_chain_map)

numbers = {'one': 1, 'two': 2}
letters = {'a': 'A', 'b': 'B'}

chain_map = ChainMap(numbers, letters) # ChainMap на основе 2х словарей
print(chain_map)
'''

# Объединение словарей с одинаковыми ключами
'''
from collections import ChainMap

for_adoption = {'dogs': 15, 'cats': 8, 'pythons': 9}
vet_treatment = {'dogs': 7, 'cats': 2, 'tigers': 3}

pets = ChainMap(for_adoption, vet_treatment) # for_adoption = 1, vet_treatment = 2

# Выведит значение по первому ключу. Т.е. по ключу из for_adoption
print(pets['dogs'])
print(pets['cats'])
'''

# Итерирование по ChainMap объекту происходит в обратном порядке от последнего указанного словаря к первому.
'''
from collections import ChainMap

numbers = {'one': 1, 'two': 2}
letters = {'a': 'A', 'b': 'B'}

alpha_num = ChainMap(numbers, letters)

for key in alpha_num:
    print(key, '->', alpha_num[key])

# При этом если вChainMap объекте есть повторяющиеся ключи в объединяемых словарях,
# то мы будем получать первое из значений.
'''

# Итерирование идёт с последних словарей к первым, 
# Но в каждом словаре от начала - к концу
'''
from collections import ChainMap

fruits = ChainMap({'apple': 10, 'banana': 20},
                  {'lemon': 10, 'pineapple': 15},
                  {'kiwi': 15, 'lime': 5})

print(*fruits)


from collections import ChainMap

fruits = ChainMap({'apple': 10, 'banana': 20},
                  {'lemon': 10, 'pineapple': 15},
                  {'kiwi': 15, 'lime': 5})

print(*fruits.keys())
'''

# Изменение данных в ChainMap объекте
'''
Измениние данных можно производить только над 1 словарём в ChainMap.
В то время, как поиск будет идти по всем объектам ChainMap
'''

# 
'''
from collections import ChainMap # Counter - для поиска по меню
from collections import Counter # Counter - для подсчёта

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

menu = ChainMap(bread, meat, sauce, vegetables, toppings)
order = Counter(input().split(','))

# Определяю длину, к которой нужно будет привести каждую выводимую строку
spaces = max(map(len, order))
line_length = spaces + 3 + len(str(order.most_common(1)[0][1]))
total = 0

for ingridient, count in sorted(order.items()):
    print(f"{ingridient.ljust(spaces, ' ')} x {count}")
    total += count * menu[ingridient]

print('-' * line_length)
print(f"ИТОГ: {total}р")
'''

# 
'''
'''
