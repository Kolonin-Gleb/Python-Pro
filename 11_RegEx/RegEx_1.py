# Я в аду?
'''
Напишите программу, в которая в заданном тексте находит все телефонные номера, соответствующие следующим форматам:

7-ddd-ddd-dd-dd
8-ddd-dddd-dddd
'''

# Артур: +7-919-667-21-19, Анри: 7-hey-anri-anri, Тимур: 8-917-4864-1911

# #7-919-667-21-19
# #8-917-4864-1911

# Тимур: 7-ddd-ddd-dd-dd, Сослан: 8-ddd-dddd-dddd, Артур: 7-123-123-11-22,,,, Дима: 8-123-123-11-22, Анри: 8-123-1231-1221...... Гвидо: 7-123-1231-1221, 7-123-13-181-22, 8-1237-131-1221

# #7-123-123-11-22
# #8-123-1231-1221


'''
from re import search
pattern1 = r'(7-\d{3}-\d{3}-\d{2}-\d{2})'
pattern2 = r'(8-\d{3}-\d{4}-\d{4})'

inp = input()
# inp = "Перезвони мне, пожалуйста: 7-919-667-21-19"
# inp = "Артур: +7-919-667-21-19, Анри: 7-hey-anri-anri, Тимур: 8-917-4864-1911"
phones = []
match = True

while True:
    match1 = search(pattern1, inp)
    match2 = search(pattern2, inp)

    if match1 == None and match2 == None:
        break
    elif match1 != None and match2 == None:
        match = match1
    elif match1 == None and match2 != None:
        match = match2
    else:
        if match1.start() < match2.start():
            match = match1
        else:
            match = match2
    
    phones.append(inp[match.start():match.end()])

    inp = inp[match.end():]
  
print(*phones, sep="\n")
'''

# Более элегантный вариант
'''
import re

st = input()
regex = r'7-\d{3}-\d{3}-\d{2}-\d{2}|8-\d{3}-\d{4}-\d{4}'
reg = re.findall(regex, st)

print(*reg, sep='\n')
'''

# 
'''
'''
import re

st = "I have these files: caaat.png, acab.txt, cat.jpeg, tca-ca.txt, na1.csv, ca2.csv"
regex = r'ca[a-e]|ca[1-5]'
reg = re.findall(regex, st)

print(len(reg))
print(*reg, sep='\n')

