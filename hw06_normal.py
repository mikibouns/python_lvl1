__author__ = 'Матиек Игорь Николаевич'

# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:
    def __init__(self, armor, damage, health = 100):
        self.armor = armor
        self.damage = damage
        self.health = health

    def take_damage(self,enemy):
        self.health -= enemy.damage() / self.armor
        print('{} -> {}'.format(self.health, self))

    def attack(self, player):
        player.take_damage()

class Player(Person):
    pass

class Enemy(Person):
    pass

p1 = Player(100, 30, 100)
e1 = Enemy(100, 30)
p1.attack(e1)