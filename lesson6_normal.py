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
import random
class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def _income_damage(self, damage):
        if self.armor > 0:
            self.armor = self.armor - int(damage*random.uniform(1, 10))
            if self.armor <= 0:
                self.armor = 0
        else:
            self.health = self.health - int(damage*random.uniform(1, 10))
            if self.health <= 0:
                self.health = 0

        print('{} получил удар, осталось: {} здоровья, {} защиты'.format(self.name, self.health, self.armor))

    def punch(self, person):
        person._income_damage(self.damage)


class Player(Person):
    def __init__(self, name, health, damage, armor):
        Person.__init__(self, name, health, damage, armor)


class Enemy(Person):
    def __init__(self, name, health, damage, armor):
        Person.__init__(self, name, health, damage, armor)


player = Player('Bob player', 100, 10, 10)
enemy = Enemy('Evil enemy', 100, 30, 100)
while player.health > 0 and enemy.health > 0:
    player.punch(enemy)
    if enemy.health <= 0:
        print('Победитель: {}.'.format(player.name))
        break
    enemy.punch(player)
    if player.health <= 0:
        print('Победитель: {}'.format(enemy.name))
        break

