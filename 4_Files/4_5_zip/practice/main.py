# step 14 Количество файлов

# выводит единственное число — количество файлов в этом архиве.
# Папка != файл
'''
from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    files_counter = 0
    for el in zip_file.namelist():
        if el.find('.') != -1:
            files_counter += 1

    print(files_counter)
'''

# step 15 Объём файлов
'''
from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    # infolist() - получение всех ФАЙЛОВ из архива с возможностью
    # получения инфы о них через свойства

    compressed_size = 0
    original_size = 0

    info = zip_file.infolist()
    
    for file in info:
        original_size += file.file_size
        compressed_size += file.compress_size

print(f"Объем исходных файлов: {original_size} байт(а)")
print(f"Объем сжатых файлов: {compressed_size} байт(а)")
'''

# step 16 Наилучший показатель
# Напишите программу, которая ВЫВОДИТ НАЗВАНИе ФАЙЛА из этого архива, который имеет наилучший показатель степени сжатия.
'''

# TODO: Разобраться позже
import zipfile # Чтобы в функции указать подсказку для типа принимаемого значения
from zipfile import ZipFile # Для работы с архивами
import os # Для получения имени файла из пути


def get_compression_ratio(file: zipfile.ZipInfo):
    if file.compress_size == file.file_size: # Сжатие не произошло
        return 0
    return file.compress_size / file.file_size * 100
    

with ZipFile('workbook.zip') as zip_file:
    best_compression_ratio = 0
    bcr_filename = ''
    info = zip_file.infolist() # Нужен метод, что вернёт только файлы без папок
    for file in info:
        if not file.is_dir():
            if best_compression_ratio < get_compression_ratio(file):
                best_compression_ratio = get_compression_ratio(file)
                bcr_filename = os.path.basename(file.filename)

    print(bcr_filename)
    print(best_compression_ratio)
'''
'''
Всегда ли коэф. сжатие верно рассчитывается по формуле:
file.compress_size / file.file_size * 100

Ведь если compress_size == file_size, то результат будет 100, хотя на самом деле
файл во все не удалось сжать!
'''

# step 18
# Форматированный вывод
'''
выводит названия всех файлов из этого архива в алфавитном порядке, 
указав для каждого его дату изменения, а также объем до и после сжатия, в следующем формате:
Alexandra Savior – Crying All the Time.mp3
  Дата модификации файла: 2021-11-30 13:27:02
  Объем исходного файла: 5057559 байт(а)
  Объем сжатого файла: 5051745 байт(а)

from zipfile import ZipFile # Для работы с архивами
import os # Для получения имени файла из пути
from datetime import datetime # Для красивого вывода даты и времени
res_d = {}

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist() # infolist() - получение списка объектов, описывающих файлы в архиве
    for file in info:
        if not file.is_dir():
            res_d.setdefault(os.path.basename(file.filename), [datetime(*file.date_time).strftime("%Y-%m-%d %H:%M:%S"), file.file_size, file.compress_size])

    # Сортировка словаря по ключам и вывод
    # нужно сортировать по названиям в lower case, но выводить оригинальные названия файлов
    lowered_keys = [key.lower() for key in res_d.keys()]
    original_keys = res_d.keys()

    # Словарь вида:
    # ключ для сортировки - ключ для вывода
    keys_d = dict(zip(lowered_keys, original_keys))
    for key in sorted(lowered_keys):
        original_key = keys_d[key]
        values = res_d[original_key]
        print(original_key)
        print(f"  Дата модификации файла: {values[0]}")
        print(f"  Объем исходного файла: {values[1]} байт(а)")
        print(f"  Объем сжатого файла: {values[2]} байт(а)")
        print()
'''

from zipfile import ZipFile

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py','test.py']


