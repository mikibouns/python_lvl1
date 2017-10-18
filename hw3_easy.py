__author__ = 'Матиек Игорь Николаевич'

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

name, age, city = input('Введите Имя, количество лет и город проживания: ').split()
def formatting_user_data(name, age, city):
    return '{}, {} год(а), проживает в городе {}'.format(name.title(), age, city.title())
print(formatting_user_data(name, age, city))

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них
# max_number = max()

x = (input('Enter three numbers: ').split())
def max(x):
    max_number = 0
    for i in x:
        i = int(i)
        if i > max_number:
            max_number = i
    return max_number

max_number = max(x)
print(max_number)

a, b, c = input('Enter three numbers: ').split()
def max2(*args):
    max_number = 0
    for i in args:
        i = int(i)
        if i > max_number:
            max_number = i
    return max_number

max_number = max2(a, b, c)
print(max_number)

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def longest_string (*args):
    max_string = ''
    for i in args:
        if len(i) > len(max_string):
            max_string = i
    return max_string

print(longest_string('fdfasdfdsafsfddsa', 'fsdfsdfsd', 'dd', 'fsdfsdfsdfsd', 'fsdfsd', '12388'))