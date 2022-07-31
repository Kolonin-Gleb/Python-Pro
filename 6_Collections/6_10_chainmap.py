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

# Теория ChainMap 2
'''
Все словари объекта ChainMap хранятся во внутреннем списке
Этот спиосок можно получить через аттрибут maps
'''

'''
from collections import ChainMap

for_adoption = {'dogs': 15, 'cats': 8, 'pythons':9}
vet_treatment = {'dogs': 7, 'cats': 2, 'tigers': 3}

pets = ChainMap(for_adoption, vet_treatment)
print(pets.maps) # Получение списка словарей

# Над этим списком можно проводить операции
pets.maps.reverse()
pets.maps[0]['lions'] = 10
del pets.maps[1]['cats']

print(pets.maps)

# Используя аттрибут maps можно ИЗМЕНЯТЬ все словари ChainMap
# Также можно провести полную иттерацию, а не по уникальным 

for animals in pets.maps:
    for key, value in animals.items():
        print(key, '->', value)
'''

# Метод new_child()
'''
# ChainMap с новым словарём по 0 индексу
# Если () - пустой словарь
# Если ({...}) - переданный словарь

from collections import ChainMap

dad = {'name': 'Timur', 'age': 29}
mom = {'name': 'Rosaly', 'age': 28}

old_family = ChainMap(dad, mom)

son = {'name': 'Solan', 'age': 0}

print(type(old_family.new_child(son)))
# Метод new_child() - возращает изменённый Объект ChainMap 
# Он НЕ изменяет вызывающий!
new_family = old_family.new_child(son)

print(old_family)
'''

# Атрибут parents
'''
# Возращает ChainMap, без 1 словаря.
# Полезно, для пропуска 1ого словаря при поиске ключей

from collections import ChainMap

dad = {'name': 'Timur', 'age': 29}  # 2
mom = {'name': 'Rosaly', 'age': 28} # 3
son = {'name': 'Soslan', 'age': 0}  # 1

family = ChainMap(son, dad, mom)

print(family)
family = family.parents
print(family)
print(type(family.parents))
'''

# Как производится сравнение ChainMap-ов
'''
from collections import ChainMap

cm1 = ChainMap({'a': 10, 'b': 20})
cm2 = ChainMap({'b': 20, 'a': 10})

print(cm1 == cm2)
print(dict(cm1.items()) == dict(cm2.items()))
'''

# Функция get_all_values()
'''
from collections import ChainMap

def get_all_values(chainmap: ChainMap, key):
    answer = set()

    # Провести полную иттерации (по всем словорям) используя .maps
    for dict in chainmap.maps:
        for iter_key, value in dict.items():
            if key == iter_key:
                answer.add(value)
    
    return answer

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'name')

print(*sorted(result))
# Arthur Timur
'''

# deep_update()
'''

from collections import ChainMap

def deep_update(chainmap, key, value):
    if key in chainmap:
        [dct.update({key: value}) for dct in chainmap.maps if key in dct]
    else:
        chainmap[key] = value
'''

# get_value()
'''
'''

from collections import ChainMap

def get_value(chainmap, key, from_left=True):
    return chainmap.get(key) if from_left else ChainMap(*chainmap.maps[::-1]).get(key)


