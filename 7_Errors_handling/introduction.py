'''
blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2}, 
              {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
              {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3}, 
              {'Comments': 4, 'Shares': 2}, 
              {'Photos': 8, 'Comments': 1, 'Shares': 1}, 
              {'Photos': 3, 'Likes': 19, 'Comments': 3}]

total_likes = 0

for post in blog_posts:
    try:
        total_likes += post['Likes']
    except KeyError:
        total_likes -= 1

print(total_likes)
'''

'''
food = ['chocolate', 'chicken', 'corn', 'sandwich', 'soup', 'potatoes', 'beef', 'lox', 'lemonade']
fifth = []

for x in food:
    try:
        fifth.append(x[4])
    except IndexError:
        fifth.append('_')
print(fifth)

100
i'm number!
10
[1, 99]
1.1
{'math', 'physics'}
'''

'''
import sys

summa = 0
not_numeric = 0

for line in sys.stdin:
    try:
        summa += float(line.strip())
    except ValueError:
        not_numeric += 1


if int(summa) == summa:
    print(int(summa))
else:
    print(float(summa))

print(not_numeric)
'''

'''
Через 2 try-except

import sys
s, counter = 0, 0
for line in sys.stdin:
    try:
        s += int(line)
    except ValueError:
        try:
            s += float(line)
        except ValueError:
            counter += 1
print(s)
print(counter)
'''

'''
months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

try:
    num = int(input())
    print(months[num])
except ValueError:
    print('Введено некорректное значение')
except KeyError:
    print('Введено число из недопустимого диапазона')
'''

'''
try:
    file = open(input(), 'r', encoding='utf-8')
    try:
        print(file.read())
    finally:
        file.close()
except FileNotFoundError:
    print("Файл не найден")
'''
'''
def add_to_list_in_dict(data: dict, key, element):
    try:
        data[key].append(element)
    except KeyError:
        data.setdefault(key, [element])


data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
add_to_list_in_dict(data, 'b', 7)

print(data)

# {'a': [1, 2, 3], 'b': [4, 5, 6, 7]}
'''

week = {
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "Воскресенье",
}

def get_weekday(number: int):
    if number < 1 or number > 7:
        raise ValueError("Аргумент не принадлежит требуемому диапазону")
    elif type(number) != int:
        raise TypeError("Аргумент не является целым числом")
    else:
        return week[number]
    

try:
    print(get_weekday('hello'))
except Exception as err:
    print(err)
    print(type(err))
# Аргумент не является целым числом
# <class 'TypeError'>

try:
    print(get_weekday(8))
except ValueError as err:
    print(err)
    print(type(err))
# Аргумент не принадлежит требуемому диапазону
# <class 'ValueError'>
