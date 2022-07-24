# from zipfile import ZipFile

# with ZipFile('test.zip') as zip_file:
    # zip_file.printdir() # Вывод таблицы с инфой о содержимом архива
    
    # infolist() - получение списка файлов из архива с
    # возможностью дальнейшего получения доп. информации о них
'''
    info = zip_file.infolist()
    print(info[6].file_size)     # размер начального файла
    print(info[6].compress_size) # размер сжатого файла
    print(info[6].filename)      # имя файла
    print(info[6].date_time)     # дата изменения файла
'''
    # namelist() - список имен файлов в архиве
'''
    info = zip_file.namelist()
    print(type(info))
    print(*info, sep='\n')
'''
    # getinfo() - получение инфы о файле в архиве по его имени
'''
    info = zip_file.namelist()
    file = zip_file.getinfo(info[4])
    print(file.file_size)
    print(file.compress_size)
    print(file.filename)
    print(file.date_time)
'''

# Работа с конкретными файлами из архива
'''
with ZipFile('test.zip') as zip_file:
    with zip_file.open('test/Разные файлы/astros.json') as file:
        print(file.read().decode('utf-8')) # Чтение файла в текстовом виде с кодировкой.
        # По умолч. ZipFile.open() открывает файлы в бинарном виде.
'''

# Запись в zip архив
'''
from zipfile import ZipFile

# Режим = w - создание архива
with ZipFile('archieve.zip', mode='w') as zip_file:
    # Имя файла для архивации, имя файла в архиве
    zip_file.write('program.py', 'arcprogram.py')

    # Посмотреть содержимое архива
    print(zip_file.namelist())
'''

# Извлечение из zip в каталог
'''
from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    # Извлечение файлов
    zip_file.extract('test/Картинки/avatar.png')
    zip_file.extract('test/Программы/image_util.py')
    zip_file.extract('test/Разные файлы/astros.json')
    # При извлечении структура архива сохраняется
'''

'''
from zipfile import ZipFile

zip_file = open('test.zip')
print(type(zip_file))

with ZipFile('test.zip') as zip_file:
    print(type(zip_file))

zip_file = ZipFile('test.zip')
print(type(zip_file))


with open('test.zip') as zip_file:
    print(type(zip_file))
'''
