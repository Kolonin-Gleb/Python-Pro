# re.split() - разбивает строку на подстроки используя регулярное выражение в качестве разделителя
# возращает список
'''
import re

result = re.split(pattern=r"[,;.]", string="foo,bar.baz;qux;stepik,beegeek")

print(result)
'''

# Почему тут выдаёт такой результат?
import re
result = re.split(r'\D+', '1 + 2 - 3 =')

print(result)

