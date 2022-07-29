'''
Тип defaultdict ведет себя почти так же, как обычный словарь dict, 
но если мы попытаемся получить доступ (или изменить значение) по несуществующему ключ, 
то defaultdict автоматически создаст ключ и сгенерирует для него значение по умолчанию.
'''

'''
from collections import defaultdict
info = defaultdict(int) # создаем словарь с типом по умолчанию int
# Т.е. все ключи, которых нет в словаре, при обращении будут получать 
# значение по умолчанию от типа int

info['name'] = 'Timur'
info['age'] = 29
info['job'] = 'Teacher'

print(info['salary'])
print(info)
'''

# Значением по умолчанию для defaultdict можно установить любое значение, исп. функцию вида
'''
from collections import defaultdict

def get_default():
    return 24

info = defaultdict(get_default, {'name': 'Timur', 'age': 29, 'job': 'Teacher'}) # Также можно задать словарь, что будет создаваться по умолчанию

print(info['salary'])

# Или через lambda
info = defaultdict(lambda: '100$', {})
print(info['salary'])
'''

# Функцию устанавливающую значение по умолчанию можно менять через аттрибут
'''
from collections import defaultdict

data = defaultdict(int)
print(data['salary1'])

data.default_factory = list
print(data['salary2'])

data.default_factory = float
print(data['salary3'])
'''

'''
from collections import defaultdict

data = defaultdict()

for func in reversed([list, int, dict, set]):
    data.default_factory = func
    
print(data['key'])
'''

# Отсортировать продукты по алфавиту
'''
from collections import defaultdict

data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145), ('Courses', 1061), ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041), ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729), ('Tutorials', 977), ('Books', 656)]
data.sort()

sales_stats = defaultdict(int)

for sale in data:
    sales_stats[sale[0]] += sale[1]

for product, income in sales_stats.items():
    print(f"{product}: ${income}")
'''

# 
'''
from collections import defaultdict

staff = [('Sales', 'Robert Barnes'), ('Developing', 'Thomas Porter'), ('Accounting', 'James Wilkins'), ('Sales', 'Connie Reid'), ('Accounting', 'Brenda Davis'), ('Developing', 'Miguel Norris'), ('Accounting', 'Linda Hudson'), ('Developing', 'Deborah George'), ('Developing', 'Nicole Watts'), ('Marketing', 'Billy Lloyd'), ('Sales', 'Charlotte Cox'), ('Marketing', 'Bernice Ramos'), ('Sales', 'Jose Taylor'), ('Sales', 'Katie Warner'), ('Accounting', 'Steven Diaz'), ('Accounting', 'Kimberly Reynolds'), ('Accounting', 'John Watts'), ('Accounting', 'Dale Houston'), ('Developing', 'Arlene Gibson'), ('Marketing', 'Joyce Lawrence'), ('Accounting', 'Rosemary Garcia'), ('Marketing', 'Ralph Morgan'), ('Marketing', 'Sam Davis'), ('Marketing', 'Gail Hill'), ('Accounting', 'Michelle Wright'), ('Accounting', 'Casey Jenkins'), ('Sales', 'Evelyn Martin'), ('Accounting', 'Aaron Ferguson'), ('Marketing', 'Andrew Clark'), ('Marketing', 'John Gonzalez'), ('Developing', 'Wilma Woods'), ('Sales', 'Marie Cooper'), ('Accounting', 'Kay Scott'), ('Sales', 'Gladys Taylor'), ('Accounting', 'Ann Bell'), ('Accounting', 'Craig Wood'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Mario Reynolds'), ('Marketing', 'Helen Taylor'), ('Marketing', 'Mary King'), ('Accounting', 'Jane Jackson'), ('Marketing', 'Carol Peters'), ('Sales', 'Alicia Mendoza'), ('Accounting', 'Edna Cunningham'), ('Developing', 'Joyce Rivera'), ('Sales', 'Joseph Lee'), ('Sales', 'John White'), ('Marketing', 'Charles Bailey'), ('Sales', 'Chester Fernandez'), ('Sales', 'John Washington')]
# Отделы должны быть расположены в лексикографическом порядке, каждый на отдельной строке, в следующем формате:
staff.sort()

# Названия департаментов должны становится ключами в словаре, если они новые
# Получать значение 1 по умолч, и +1 иначе
sales_stats = defaultdict(int)

for employee in staff:
    sales_stats[employee[0]] += 1

for dep, workers_count in sales_stats.items():
    print(f"{dep}: {workers_count}")
'''

# Отделы, а также имена и фамилии сотрудников в этих отделах, должны быть расположены по алфавиту
# Сотрудники могут повторяться
# Каждый отдел на отдельной строке!
'''
staff_broken = [('Developing', 'Miguel Norris'), ('Sales', 'Connie Reid'), ('Sales', 'Joseph Lee'), ('Marketing', 'Carol Peters'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Ann Bell'), ('Marketing', 'Ralph Morgan'), ('Accounting', 'Gloria Higgins'), ('Developing', 'Wilma Woods'), ('Developing', 'Wilma Woods'), ('Marketing', 'Bernice Ramos'), ('Marketing', 'Joyce Lawrence'), ('Accounting', 'Craig Wood'), ('Developing', 'Nicole Watts'), ('Sales', 'Jose Taylor'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Edna Cunningham'), ('Sales', 'Jose Taylor'), ('Marketing', 'Helen Taylor'), ('Accounting', 'Kimberly Reynolds'), ('Marketing', 'Mary King'), ('Sales', 'Joseph Lee'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Andrew Clark'), ('Accounting', 'John Watts'), ('Accounting', 'Rosemary Garcia'), ('Accounting', 'Steven Diaz'), ('Marketing', 'Mary King'), ('Sales', 'Gladys Taylor'), ('Developing', 'Thomas Porter'), ('Accounting', 'Brenda Davis'), ('Sales', 'Connie Reid'), ('Sales', 'Alicia Mendoza'), ('Marketing', 'Mario Reynolds'), ('Sales', 'John White'), ('Developing', 'Joyce Rivera'), ('Accounting', 'Steven Diaz'), ('Developing', 'Arlene Gibson'), ('Sales', 'Robert Barnes'), ('Sales', 'Charlotte Cox'), ('Accounting', 'Craig Wood'), ('Marketing', 'Carol Peters'), ('Marketing', 'Ralph Morgan'), ('Accounting', 'Kay Scott'), ('Sales', 'Evelyn Martin'), ('Marketing', 'Billy Lloyd'), ('Sales', 'Gladys Taylor'), ('Developing', 'Deborah George'), ('Sales', 'Charlotte Cox'), ('Marketing', 'Sam Davis'), ('Sales', 'John White'), ('Sales', 'Marie Cooper'), ('Marketing', 'John Gonzalez'), ('Sales', 'John Washington'), ('Sales', 'Chester Fernandez'), ('Sales', 'Alicia Mendoza'), ('Sales', 'Katie Warner'), ('Accounting', 'Jane Jackson'), ('Sales', 'Chester Fernandez'), ('Marketing', 'Charles Bailey'), ('Marketing', 'Gail Hill'), ('Accounting', 'Casey Jenkins'), ('Accounting', 'James Wilkins'), ('Accounting', 'Casey Jenkins'), ('Marketing', 'Mario Reynolds'), ('Accounting', 'Aaron Ferguson'), ('Accounting', 'Kimberly Reynolds'), ('Sales', 'Robert Barnes'), ('Accounting', 'Aaron Ferguson'), ('Accounting', 'Jane Jackson'), ('Developing', 'Deborah George'), ('Accounting', 'Michelle Wright'), ('Accounting', 'Dale Houston')]
staff = sorted(list(set(staff_broken))) # Починка + сортировка

from collections import defaultdict

department_workers = defaultdict(list)

for dep, emp in staff:
    department_workers[dep].append(emp)

for dep, emps in department_workers.items():
    print(f"{dep}: ", end='')
    for i in range(len(emps)-1):
        print(emps[i], end=', ')
    print(emps[-1])
'''

# 
'''
победитель проигравыший

from collections import defaultdict

def wins(pairs: list):
    player_defeated = defaultdict(set)
    
    for pair in pairs:
        player_defeated[pair[0]].add(pair[1])

    return player_defeated

result = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])

# Вывод
# for winner, losers in sorted(result.items()):
#     print(winner, '->', *sorted(losers))
'''

# Функция best_sender()
'''
Функция должна определять отправителя, имеющего наибольшее количество слов,
и возвращать его имя.
Если таких отправителей несколько, следует вернуть имя того,
чье имя больше по алфавиту (сортировка по убыванию).

План:
Сделаю defaultdict
где ключ - имя отправителя
значение - число отправленных слов

Потом нужно будет получить ключи с максимальными значениями из словаря.
- Для этого найду максимальное значение, а затем выберу все ключи с ним

Вывести ответ
'''

'''
from collections import defaultdict

def best_sender(mesagges: list, senders: list):
    sender_words = defaultdict(int)
    for sender, message in zip(senders, mesagges):
        sender_words[sender] += len(message.split())
    
    max_messages = max(sender_words.values()) # Получение макс. числа сообщений

    best_senders = [sender for sender in sender_words.keys() if sender_words[sender] == max_messages] # Выборка всех отправителей с этим макс. числом сообщений
    return(sorted(best_senders, reverse=True)[0])

messages = ['How is Stepik for everyone', 'Stepik is useful for practice']
senders = ['Bob', 'Charlie']

print(best_sender(messages, senders))
'''

# flip_dict()
'''
Функция должна возвращать новый словарь (тип defaultdict с типом list в качестве значения по умолчанию),
который представляет собой «перевернутый» словарь dict_of_lists.

План:
Нужно собрать все значения из полученного словаря в список. -> Они потом будут использоваться в качестве ключей
Каждый ключ (из знач) получает в качестве значения список из всех предыдущих ключей + свой)


'''

from collections import defaultdict

def flip_dict(dict_of_lists: dict) -> defaultdict:
    answer = defaultdict(list)
    
    return answer


data = {'Arthur': ['cacao', 'tea', 'juice'], 'Timur': ['coffee', 'tea', 'juice'], 'Anri': ['juice', 'coffee']}

# Вывод
for key, values in flip_dict(data).items():
    print(f'{key}: {", ".join(values)}')

'''
cacao: Arthur
tea: Arthur, Timur
juice: Arthur, Timur, Anri
coffee: Timur, Anri
'''
