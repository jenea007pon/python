# EASY
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import sys
import shutil

i = 1
while i < 10:
    os.mkdir(("dir_" + str(i)))
    i += 1

i = 1
while i < 10:
    os.rmdir(("dir_" + str(i)))
    i += 1
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def show_only_dir():
    for el in os.listdir():
        if os.path.isdir(el) == True:
            print(el)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
shutil.copyfile(os.path.basename(sys.argv[0]), str(os.path.basename(sys.argv[0]) + '_copy.py'))

# для normal

def change_dir():
    # 1. Перейти в папку
    try:
        path = input("Введите имя или путь к директории: ")
        os.chdir(path)
    except:
        print('Не удалось перейти в папку')
    else:
        print('Директория успешно изменена')


def show_content():
    # 2. Просмотреть содержимое текущей папк
    print(os.listdir())

def remove_dir():
    # 3. Удалить папку
    try:
        path = input("Введите имя или путь к директории: ")
        os.rmdir(path)
    except:
        print('Не удалось удалить директорию. Или она содержит файлы или имя\путь указаны неправильно.')
    else:
        print('Директория успешно удалена.')


def create_dir():
    # 4. Создать папку
    try:
        path = input("Введите имя или путь к директории: ")
        os.mkdir(path)
    except:
        print('Не удалось создать папку.')
    else:
        print('Папка успешно создана')







