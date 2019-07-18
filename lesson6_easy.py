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
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина повернула ', direction)


class TownCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(Car, speed, color, name)

    @property
    def is_police(self):
        return False

class SportCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(Car, speed, color, name)

    @property
    def is_police(self):
        return False

class WorkCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(Car, speed, color, name)

    @property
    def is_police(self):
        return False


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(Car, speed, color, name)

    @property
    def is_police(self):
        return True

car1 = TownCar('80 km', 'Red', 'Mersedes')
print(car1.is_police, car1.go(), car1.turn('Направо'), car1.stop())

car2 = PoliceCar('80 km', 'Red', 'Lada')
print(car2.is_police)


