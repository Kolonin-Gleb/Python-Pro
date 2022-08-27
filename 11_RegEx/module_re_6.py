from re import search

# search возращает позицию первого удачного поиска.

match1 = search('super', 'superstition again superstition')
match2 = search('super', 'without')

print(match1) # span(0, 5) - индекс начального и конечного вхождения (невключительно)
print(match2) # None - не найдено

match3 = search('[a-z]+', '123foFo456')
match4 = search('\d+', 'foo.bar')

print(match3)
print(match4)

# match - начало строки должно совпадать с паттерном

from re import match

match5 = match('super', 'superstition')
match6 = match('super', 'insuperable')

print(match5)
print(match6)

