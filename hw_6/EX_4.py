"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
"""


class Car:

    def __init__(self):
        self.speed = int(input('Введите скорость: '))
        self.color = input('Введите цвет: ')
        self.name = input('Введите название: ')
        self.is_police = input('Если этот автомобиль полицейсский введите "y", иначе "n": ').lower()
        if self.is_police == 'y':
            self.is_police = True
        elif self.is_police == 'n':
            self.is_police = False
        self.show_speed_car = int(input('Введите текущую скорость автомобиля: '))

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        self.direction = input('Если хотите, чтоб машина повернула налево, введите "left", направо "right"').lower()
        if self.direction == 'left':
            print('Машина повернула налево')
        elif self.direction == 'right':
            print('Машина повернула направо')

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.show_speed_car}')


class TownCar(Car):
    """Городские авто"""

    def __init__(self):
        super().__init__()

    def show_speed(self):
        if self.show_speed_car > 60:
            print('Превышение скорости!!!')
        else:
            print(f'Текущая скорость автомобиля: {self.show_speed_car}')


class SportCar(Car):
    """Спортивные авто"""


class WorkCar(Car):
    """Рабочие авто"""

    def __init__(self):
        super().__init__()

    def show_speed(self):
        if self.show_speed_car > 40:
            print('Превышение скорости!!!')
        else:
            print(f'Текущая скорость автомобиля: {self.show_speed_car}')


class PoliceCar(Car):
    """Полицейские авто"""


car_two = TownCar()
print(car_two.speed)
print(car_two.color)
print(car_two.is_police)
print(car_two.show_speed_car)
car_two.go()
car_two.stop()
car_two.turn()
car_two.show_speed()
