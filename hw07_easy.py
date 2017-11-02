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
            print('------- Ваша карточка -------')
        elif self.__class__.__name__ == 'Computer':
            print('---- Карточка компьютера ----')
        else:
            print('-----------------------------')
        func(self)
        print('-----------------------------')

    return wrapper


class Card:
    def __init__(self):
        self.card = []

    def _sort_card(self):
        temporary_card = []
        while len(temporary_card) < 20:
            random_card_number = random.randrange(1, 91)
            if random_card_number in temporary_card:
                continue
            temporary_card.append(random_card_number)
        return sorted(temporary_card)

    def create_card(self):
        for i in range(0, 20, 5):
            section_card = self._sort_card()[i: i + 5]
            while section_card.count(' ') != 5:
                index_card = random.randrange(0, 5)
                section_card[index_card: index_card + 1] += [' ']
            self.card += section_card

    @card_format
    def print_card(self):
        for i in range(0, 40, 10):
            for j in self.card[i: i + 10]:
                print('{:>2}'.format(j), end=' ')
            print()

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


class Game:
    def __init__(self, player, computer, bag_with_kegs):
        self.player = player
        self.computer = computer
        self.bab_with_kegs = bag_with_kegs

    @staticmethod
    def answer():
        while True:
            answer = input('Зачеркнуть цифру? (y/n) ')
            if answer == 'y' or answer == 'n':
                break
        return answer

    def start_game(self):
        self.player.create_card()
        self.computer.create_card()
        while True:
            if self.player.card.count('-') == 20 or self.computer.card.count('-') == 20 or len(self.bab_with_kegs.bag_with_kegs) <= 1:
                self._finish_game()
                break
            keg_number = self.bab_with_kegs.get_keg()
            print('Новый боченок: {} (осталось {})'.format(keg_number, len(self.bab_with_kegs.bag_with_kegs)))
            self.player.print_card()
            self.computer.print_card()
            self.computer.cross_out_number(keg_number)
            answer = Game.answer()
            if answer == 'y':
                if self.player.cross_out_number(keg_number):
                    continue
                else:
                    print('Ты проиграл! Будь внимательным!')
                    break
            else:
                if keg_number in self.player.card:
                    print('Ты проиграл! Будь внимательным!')
                    break


    def _finish_game(self):
        player = self.player.card.count('-')
        computer = self.computer.card.count('-')
        if player > computer:
            print('Ты победил!')
        elif player == computer:
            print('Ничья!')
        else:
            print('Ты проиграл!')



def main():
    game = Game(Player(), Computer(), BagWithKegs())
    game.start_game()


if __name__ == '__main__':
    main()
