__author__ = 'Матиек Игорь Николаевич'

# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, speed=0, color=None, name=None, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if self.is_police == True:
            print('Полицейский автомобиль')


    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction=None):
        if direction == None:
            print('Машина едет прямо')
        else:
            print('Машина поаернула на {}'.format(direction))

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__()
        print('Городской автомобиль')

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__()
        print('Спортивный автомобиль')

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__()
        print('Рабочий автомобиль')

class PoliceCar(Car):
    pass

polCar = PoliceCar(120, 'red', 'renault', True)
worCar = WorkCar(150, 'blue', 'opel')
worCar.go()

