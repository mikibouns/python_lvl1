__author__ = 'Матиек Игорь Николаевич'

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

import os

def go_to_dir():
    print('Чтобы вернуться в предыдущую папку введите: <')
    dir_name = input('Введите имя папки: ')
    if os.path.isdir(os.path.join(os.getcwd(), dir_name)):
        os.chdir(dir_name)
    elif dir_name == '<':
        os.chdir(os.path.dirname(os.getcwd()))
    else:
        print('!!!Папка не найдена!!!')

def current_dir_contents():
    print('Содержимое текущей папки ({})'.format(os.getcwd()))
    for i in os.listdir(os.getcwd()):
        if os.path.isdir(os.path.join(os.getcwd(), i)):
            print('dir >>', i)
        else:
            print('file >>', i)

def del_dir():
    dir_name = input('Введите имя папки: ')
    try:
        os.rmdir(dir_name)
        print('Папка {} успешно удалена'.format(dir_name))
    except FileExistsError:
        print('!!!Папка не найдена!!!')

def create_dir():
    dir_name = input('Введите имя папки: ')
    try:
        os.mkdir(dir_name)
        print('Папка {} успешно создана'.format(dir_name))
    except FileExistsError:
        print('!!!Папка уже существует!!!')
    except OSError:
        print('!!!Не корректное имя папки. Папка не создана!!!')

def main():
    while True:
        print('''
        ---------------------------------------------
        | 1. Перейти в папку                        |
        | 2. Просмотреть содержимое текущей папки   |
        | 3. Удалить папку                          |
        | 4. Создать папку                          |
        | 5. Выйти                                  |
        ---------------------------------------------
        ''')

        print('Текущая путь: {}'.format(os.getcwd()))
        menu_item = input('Введите необходимый пункт: ')
        if menu_item == '1':
            go_to_dir()
        elif menu_item == '2':
            current_dir_contents()
        elif menu_item == '3':
            del_dir()
        elif menu_item == '4':
            create_dir()
        elif menu_item == '5':
            print('До встречи')
            break
        else:
            print('!!!Нет такого пункта меню!!!')



if __name__ == '__main__':
    main()