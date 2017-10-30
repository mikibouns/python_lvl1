__author__ = 'Матиек Игорь Николаевич'

# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный класс, который наследуется от базового - Игрушка

class ToyFactory:
    def __init__(self, name, color, type):
        if type == 'bear':
            self.toy = Bear(name, color, type)
        elif type == 'doll':
            self.toy = Doll(name, color, type)
        elif type == 'Car':
            self.toy = Car(name, color, type)
        else:
            self.toy = Toy(name, color, type)

    def get_materials(self):
        print('Закупка сырья')

    def sewing(self):
        print('Пошив')

    def painting(self):
        print('Окраска')

    def return_toy(self):
        self.get_materials()
        self.sewing()
        self.painting()
        print('Игрушка готова')
        return self.toy

class Toy:
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

    def toy_info(self):
        print('Имя игрушки: {}, Цвет игрушки: {}'.format(self.name, self.color))


class Bear(Toy):
    def toy_info(self):
        print('Тип игрушки "Мишка"')
        super().toy_info()

class Doll(Toy):
    def toy_info(self):
        print('Тип игрушки "Кукла"')
        super().toy_info()

class Car(Toy):
    def toy_info(self):
        print('Тип игрушки "Машинка"')
        super().toy_info()

create_toy = ToyFactory('Bobo', 'red', 'bear')
toy_1 = create_toy.return_toy()
toy_1.toy_info()