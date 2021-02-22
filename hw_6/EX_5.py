"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')


user_one = Pen('Карандаш')
print(user_one.title)
user_one.draw()

user_two = Pencil('Ручка')
print(user_two.title)
user_two.draw()

user_free = Handle('Маркер')
print(user_free.title)
user_free.draw()
