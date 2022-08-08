# Решение задач

# step 1
'''
import json

countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
             'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
             'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
             'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}

json_countries = json.dumps(countries, indent='   ', separators=(',', ' - '), sort_keys=True)
print(json_countries)
'''

# step 2
'''
import json

words = {
         frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
         "travel": "trævl",
         ("hello", "world"): ("həˈləʊ", "wɜːld"),
         "moonlight": "muːn.laɪt",
         "sunshine": "ˈsʌn.ʃaɪn",
         ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
         "adventure": "ədˈventʃər",
         "beautiful": "ˈbjuːtɪfl",
         frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
         "bicycle": "baisikl",
         ("pilot", "fly"): ("pailət", "flai")
        }

data_json = json.dumps(words, skipkeys=True)
# print(data_json)
'''

# step 3
'''
import json

club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
         "trainer": "Julian Nagelsmann", "gaolkeeper": "M. Neuer", "league_position": 1}

club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
         "trainer": "Xavier Creus", "gaolkeeper": "M. Ter Stegen", "league_position": 7}

club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
         "trainer": "Michael Carrick", "gaolkeeper": "D. De Gea", "league_position": 8}

data = []
data.append(club1)
data.append(club2)
data.append(club3)

with open('data.json', 'w') as file:
    json.dump(data, file, indent='   ')
'''

# step 4
'''
import json

specs = {
         'Модель': 'AMD Ryzen 5 5600G',
         'Год релиза': 2021,
         'Сокет': 'AM4',
         'Техпроцесс': '7 нм',
         'Ядро': 'Cezanne',
         'Объем кэша L2': '3 МБ',
         'Объем кэша L3': '16 МБ',
         'Базовая частота': '3900 МГц'
        }

specs_json = json.dumps(specs, indent='   ', ensure_ascii=False)

print(specs_json)
'''

# step 5
'''
import json

def is_correct_json(s:str):
    try:
        a = json.loads(s)
        return True
    except:
        return False

data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'

print(is_correct_json(data))
'''

# step 6
'''
'''


# step 7
'''
# Я хочу обойтись без создания временного списка.
# Сразу писать данные во 2 файл

import json

lst = []

with open('data.json', 'r', encoding='utf-8') as reading_file:
    data = json.load(reading_file)
    for value in data:
        if type(value) == str:
        # print(f'{value}!')
            lst.append(value+'!')
        elif type(value) == int:
        # print(value+1)
            lst.append(value+1)
        elif type(value) == bool: 
        # print(not value)
            lst.append(not value)
        elif type(value) == list:
        # print([el*2 for el in value])
            lst.append(value * 2)
        elif type(value) == dict:
            value.setdefault("newkey", None)
            lst.append(value)
        # print(value)
        elif value == None:
            continue

with open('updated_data.json', 'w', encoding='utf-8') as writing_file:
    json.dump(lst, writing_file)
'''

'''
import json
import sys

data = json.loads(sys.stdin.read())

for key, value in data.items():
    if type(value) != list:
        print(f"{key}: {value}")
    else:
        print(f"{key}: {', '.join(map(str, value))}")
'''

