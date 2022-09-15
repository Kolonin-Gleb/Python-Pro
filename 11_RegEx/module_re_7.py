# Функция findall() - возращает список всех совпадений


'''
import re
text = 'ул. Часовая, дом № 25, корпус 2, квартира 69'
print(re.findall('\d+', text)) # Список всех совпадений
'''

# Когда в RegEx для findall есть группа, возращается список соответствующих групп, а не 
# список полных совпадений с регулярным выражением
'''
import re
print(re.findall('#(\w+)#', '#foo#.#bar#.#baz#'))
'''

# Пример работы с несколькими группами
'''
import re
print(re.findall('(\w+),(\w+)', 'foo,bar,baz,qux,quux,corge')) # Формирует список кортежей по 2 эл
print(re.findall('(\w+),(\w+),(\w+)', 'foo,bar,baz,qux,quux,corge')) # Формирует список кортежей по 3 эл
'''

# Функция finditer() - возращает итератор всех совпадений
'''
from re import findall, finditer

result1 = findall(r'\w', 'beegeek')
result2 = finditer(r'\w', 'beegeek')

# *_ - позволяет опустить сколько угодно значений при распаковке контейнера
match1, *_ = result1
match2, *_ = result2

print(match1)
print(match2)
'''

# Подсчёт строк удовлетворяющих условиям в тексте
'''
'''


