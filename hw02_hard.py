__author__ = 'Матиек Игорь Николаевич'

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

# equation = 'y = -12x + 11111140.2121'
# x = 2.5
# вычислите и выведите y



# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
# date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'


# incoming_date = input('Enter date: ')
# day, month, year = incoming_date.split('.')
# if (30 >= int(day) > 0) and (12 >=int(month) > 0) and (9999 >= int(year) > 0) and (len(incoming_date) == 10):
#     print('Date is correct!')
# else:
#     print('Date is not correct!')

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

room = 10000000
countString = 0
countPosition = 1
count = 1
for i in range(1, 2000000000):
    for j in range(i):
        countString += 1
        countPosition = 1
        for x in range(i):
            countPosition += 1
            count += 1
            if count == room:
                print('{} {}'.format(countString, countPosition))
                break

#перебор конечно не самое хорошое решение)))
import time


start_time = time.time()
room_for_search = 1999999999

block = 1
first_room = 1
floor = 1

while room_for_search >= first_room + block ** 2:
    first_room = first_room + block ** 2
    floor += block
    block += 1

floor += ((room_for_search - first_room) // block)#
room_sequince = int((room_for_search - first_room) % block + 1)

print(floor, room_sequince)

finish_time = time.time()

program_execution_time = finish_time - start_time
print(program_execution_time)
