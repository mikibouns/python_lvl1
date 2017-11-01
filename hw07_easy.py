__author__ = 'Матиек Игорь Николаевич'

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""

import random


def card_format(func):
    def wrapper(self):
        if self.__class__.__name__ == 'Player':
            print('------ Ваша карточка -----')
        elif self.__class__.__name__ == 'Computer':
            print('-- Карточка компьютера ---')
        else:
            pass
        func(self)
        print('--------------------------')
    return wrapper

class Card:
    def __init__(self):
        self.card = []

    def create_card(self):
        while len(self.card) < 20:
            random_card_number = random.randrange(1, 91)
            if random_card_number in self.card:
                continue
            self.card.append(random_card_number)
        self.card.sort()


    @card_format
    def print_card(self):
        for i in range(0, 20, 5):
            print(self.card[i: i+5])

    def cross_out_number(self, keg_number):
        if keg_number in self.card:
            self.card[self.card.index(keg_number)] = '-'
            return True
        else:
            return False

class Player(Card):
    pass

class Computer(Card):
    pass

class BagWithKegs:
    def __init__(self):
        self.bag_with_kegs = [i for i in range(1, 91)]

    def get_keg(self):
        keg_index = random.randrange(1, len(self.bag_with_kegs))
        return self.bag_with_kegs.pop(keg_index)

def main():
    bag = BagWithKegs()
    player = Player()
    computer = Computer()
    player.create_card()
    computer.create_card()
    while True:
        keg_number = bag.get_keg()
        print('Новый боченок: {} (осталось {})'.format(keg_number, len(bag.bag_with_kegs)))
        player.print_card()
        computer.print_card()
        computer.cross_out_number(keg_number)
        player.cross_out_number(keg_number)
        if len(bag.bag_with_kegs) <= 1:
            break
        # answer = input('Зачеркнуть цифру? (y/n) ')
        # if answer == 'n':
        #     continue
        # elif answer == 'y' and player.cross_out_number(keg_number):
        #     continue
        # else:
        #     print('You loser!')
        #     break

    if player.card.count('-') > computer.card.count('-'):
        print('You win!')
    elif player.card.count('-') > computer.card.count('-'):
        print('Draw!')
    else:
        print('You loser!')

if __name__ == '__main__':
    main()
