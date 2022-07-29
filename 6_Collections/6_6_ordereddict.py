# Тип данных OrderedDict
'''
from collections import OrderedDict

numbers = OrderedDict()

numbers['one'] = 1
numbers['two'] = 2
numbers['three'] = 3

print(numbers)
'''

# При итеррировании по OrderedDict можно исп. встроенную функцию reversed()
'''
from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)

for key in reversed(numbers): # Словарь будет читаться в обратном порядке
    print(key, '->', numbers[key])
'''

# 
'''
from collections import OrderedDict

grades = OrderedDict(Timur=100, Arthur=84, Anri=94, Dima=98)
new_grades = OrderedDict()

for rule in (True, False, False, True):
    name, grade = grades.popitem(last=rule)
    new_grades[name] = grade
    
print(*new_grades)
'''

# 
'''
from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
data_reversed = OrderedDict()

for key in reversed(data): # Словарь будет читаться в обратном порядке
    data_reversed[key] = data[key]

print(data_reversed)
'''

# 
'''

from collections import OrderedDict

# data = OrderedDict(key1='value1', key2='value2', key3='value3', key4='value4')
data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
data_mixed = OrderedDict()

key_ind = 0
while key_ind != len(data.keys()) // 2:
    data_mixed[list(data.keys())[key_ind]] = list(data.values())[key_ind]
    key_ind += 1
    data_mixed[list(data.keys())[-key_ind]] = list(data.values())[-key_ind]

print(data_mixed)
'''
