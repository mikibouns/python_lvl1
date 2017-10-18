__author__ = 'Матиек Игорь Николаевич'

# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь name - строка полученная от пользователя,
# health - 100, damage - 50.
# Теперь надо создать функцию attack(person, person) функция в качестве аргумента будет
# принимать атакующего и атакуемого, функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого


import random

#
# player = {'name': 'player', 'health': 100, 'damage': 50, 'armor': 0.7}
# enemy = {'name': 'enemy', 'health': 200, 'damage': 30, 'armor': 0.5}
#
# def attack(player, enemy):
#     jude = random.random()
#     player['health'] = float(player['health'])
#     enemy['health'] = float(enemy['health'])
#     print(jude)
#     if jude > 0.5:
#         player['health'] -= float(enemy['damage'])
#     else:
#         enemy['health'] -= float(player['damage'])



# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 0.7
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# def return_damage(damage, armor):
#     return damage / armor


# Сохраните эти сущности, каждую в свой файл, в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

FILE_LIST = ('player.txt', 'enemy.txt')


def write_player_options(player):
    name_file = '{}.txt'.format(player['name'])
    with open(name_file, 'w', encoding='UTF-8') as file:
        for i in sorted(player.values()):
            file.write(i + '\n')


def get_player_options(file_option):
    list_key = ['armor', 'health', 'damage', 'name']
    with open(file_option, encoding='UTF-8') as file:
        player_name = [i.rstrip() for i in file]
        player_name = dict(zip(list_key, player_name))
    return player_name


def return_damage(damage, armor):
    return float(damage) / float(armor)


def attack(player, enemy):
    player['health'] = float(player['health'])
    enemy['health'] = float(enemy['health'])
    judge = random.random()
    while True:
        if judge > 0.5:
            player['health'] -= return_damage(enemy['damage'], player['armor'])
            judge = 0
            if player['health'] <= 0:
                return enemy
        else:
            enemy['health'] -= return_damage(player['damage'], enemy['armor'])
            judge = 1
            if enemy['health'] <= 0:
                return player


def main():
    player = {'name': 'player', 'health': '100', 'damage': '30', 'armor': '0.7'}
    enemy = {'name': 'enemy', 'health': '100', 'damage': '30', 'armor': '0.8'}
    write_player_options(player)
    write_player_options(enemy)
    player = get_player_options(FILE_LIST[0])
    enemy = get_player_options(FILE_LIST[1])
    winner = attack(player, enemy)
    print('Winner is {}, health: {}'.format(winner['name'].title(), int(winner['health'])))


if __name__ == '__main__':
    main()
