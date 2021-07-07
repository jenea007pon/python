#  NORMAL
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
from lesson5_easy import change_dir, show_content, remove_dir, create_dir
import os
import sys


menu = {1: '1. Перейти в папку', 2: '2. Просмотреть содержимое текущей папки', 3: '3. Удалить папку',
        4: '4. Создать папку'}
print(menu.values())
if 'help' in sys.argv:
    print(menu.values())
while True:
    userChoice = int(input('Введите действие(цифру):'))
    if userChoice == 1:
        print('Вы выбрали: 1. Перейти в папку')
        lesson5_easy.change_dir()
    elif userChoice == 2:
        print('Вы выбрали: 2. Просмотреть содержимое текущей папки')
        lesson5_easy.show_content()
    elif userChoice == 3:
        print('Вы выбрали: 3. Удалить папку')
        lesson5_easy.remove_dir
    elif userChoice == 4:
        print('Вы выбрали: 4. Создать папку')
        lesson5_easy.create_dir()
    else:
        print('Вы неверно ввели действие, попроуйте снова.')






