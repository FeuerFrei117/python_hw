"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property
"""


class Clothes:

    fabric_stand = []

    @property
    def fill_fabric(self):
        self.fabric_stand = sum(self.fabric_stand)
        return f'Будет всего потрачено ткани: {self.fabric_stand}'


class Coat(Clothes):
    def __init__(self, v):
        super().__init__()
        self.v = v

    @property
    def fabric_consumption(self):
        self.result = round(self.v / 6.5 + 0.5, 2)
        self.fabric_stand.append(self.result)
        return self.result


class Suit(Clothes):
    def __init__(self, h):
        super().__init__()
        self.h = h

    @property
    def fabric_consumption(self):
        self.result = round(2 * self.h + 0.3, 2)
        self.fabric_stand.append(self.result)
        return self.result


one_coat = Coat(5)
print(one_coat.fabric_consumption)

one_suit = Suit(5)
print(one_suit.fabric_consumption)

two_coat = Coat(5)
print(two_coat.fabric_consumption)

two_suit = Suit(5)
print(two_suit.fabric_consumption)

print(one_coat.fill_fabric)
print(two_suit.fill_fabric)
print(two_suit.fabric_stand)
