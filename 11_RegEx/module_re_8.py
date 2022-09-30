# функция sub() - для замены подстроки на строку
# re.sub(pattern, repl, string, count, flags)
# pattern - что ищем
# repl    - на что заменяем
# string  - где производится поиск
# count   - максимальное число замен
# flags   - флаги 

# Пример замены подстрки на строку
'''
import re
text = 'Java самый популярный язык программирования в 2022 году.'
res = re.sub(pattern=r'Java', repl=r'Python', string=text)

print(res)
'''

# Пример замены подстроки на строку, что встречалась ранее.
# Использование ссылки назад
'''
import re
result = re.sub(pattern=r'(\w+),bar,baz,(\w+)', repl=r'\2,bar,baz,\1', string=r'foo,bar,baz,qux')

# Происходит смена местами первого и последнего слова
print(result)
'''

# Пример замены подстроки с использованием Функции
# Если repl=функция, то 
# каждая найденная подстрока из pattern будет передаваться в эту функцию (объект Match)
# возращаемое функцией значение будет подставляться на место подстроки

'''
import re
def func(match_obj: re.Match):
    s = match_obj.group(0)         # строка совпадения
    if s.isdigit():
        return str(int(s) * 10)
    else:
        return s.upper()

# Использование функции позволяет заменять подстроку на результат её обработки.
result = re.sub(pattern=r'\w+', repl=func, string=r'foo.10.bar.20.baz30.40')

print(result)
'''

# функция sub() - для замены подстроки на строку. 
# возвращает кортеж, состоящий из измененной строки и количества сделанных замен.

'''
import re

text = 'foo.123.bar.456.baz.789.geek'

result1 = re.subn(r'\d+', r'#', text)
result2 = re.subn(r'[a-z]+', r'(*)', text, count=2)

print(result1)
print(result2)
'''

# Noramilze jpeg (to jpg)
'''
# without regex
def normalize_jpeg(filename: str) -> str:
    extension_position = filename[::-1].find('.') + 1
    return filename[-extension_position::-1][::-1] + "jpg"

# with regex
import re
def normalize_jpeg(filename):
    return re.sub(pattern=r'jpe?g$', repl=r'jpg', string=filename, flags=re.I)

print(normalize_jpeg('stepik.jPeG'))
# stepik.jpg

print(normalize_jpeg('mountains.JPG'))
# mountains.jpg

print(normalize_jpeg('windows11.jpg'))
# windows11.jpg

print(normalize_jpeg('stepik.jpeg.jpeg'))
# stepik.jpeg.jpg
'''

# Normalize whitespace - приведение отступов к правильному виду
'''
import re

def normalize_whitespace(string: str) -> str:
    return re.sub(pattern=r'\s+', repl=r' ', string=string)

print(normalize_whitespace('AAAA                A                AAAA'))
# AAAA A AAAA

print(normalize_whitespace('Тут нет лишних пробелов'))
# Тут нет лишних пробелов

print(normalize_whitespace('Тут   н   е   т     л   и     шних пробелов     '))
# Тут н е т л и шних пробелов 
'''

# Ключевые слова. Заменить все ключевые слова на <kw>
'''
import re

def replaceKeywords(obj: re.Match):
    keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
    keywords = [keyw.upper() for keyw in keywords]

    if obj.group(0).upper() in keywords:
        return "<kw>"
    else:
        return obj.group(0)

print(re.sub(pattern=r'\w+', repl=replaceKeywords, string=input())) 
'''
# Test input:
# text = 'True, assert, as, false, or, Import' 
# print(re.sub(pattern=r'\w+', repl=replaceKeywords, string=input())) 
# Correct output:
# <kw>, <kw>, <kw>, <kw>, <kw>, <kw>



# Первые буквы
# Менять первые две буквы в каждом слове, состящем из 2х и более букв

# Моё решение с использование repl=function
# Такой подход пусть и громозский, но описывает логику
'''
import re

def swapy(obj: re.Match):
    # Получить слово совпадения из объекта
    word = obj.group(0)
    if len(word) >= 2:
        word = list(word)
        # Поменять первые две буквы местами
        word[0], word[1] = word[1], word[0]
        return ''.join(word)
    else:
        return word

print(re.sub(pattern="\w+", repl=swapy, string=input()))
'''

# Более простое решение через группы
'''
import re
string = input()
print(re.sub(r'\b(\w)(\w)', r'\2\1', string))
'''


# Умножение строк
# Раскрыть все умножения и вывести результат
# ti2(Be)3(Ge) => tiBeBeGeGeGe.

# Примечание 1. * 0 => не выводить строку вовсе
# Примечание 2. Соблюдать приоритет операций bbbb10(2(a))bbb => bbbbaaaaaaaaaaaaaaaaaaaabbb

# План реализации
'''
0. В функцию подаю всю строку пользователя.
- Забираю начало и конец строки, чтобы оставить только часть вида: число()
- Выполняю обработку оставшейся центральной части

1. Здесь repl = function - однозначно
2. 


Поймать шаблоном содержимое скобок.
Если в этом содержимом есть ещё скобки поймать их.
С помощью ссылки назад посмотреть есть ли 0 * на эту скобку. 
Если да, то выкинуть это содержимое.
Если нет, то выполнить умножение и замену на полученный результат
'''

import re

# TODO: Я решил вернуться к этому позже.
# Возможно я изучив тему лучше я смогу придумать более простой способ
def process_string(text: str) -> str:
    if text.find("(") == -1:
        return text

    start_until = text.find("(") - 1
    start_part = text[:start_until]

    end_from = text[::-1].find(")")
    end_part = text[-end_from:]

    print(text[start_until:-end_from])
    # В полученном тексте необходимо:
    # - Проверить наличие вложенных скобок
    # 


process_string("hello3(world)hi")

def multiply_string(word: str) -> str:
    return "str"


# print(re.sub(pattern=r"", repl=multiply_string, string=r""))

