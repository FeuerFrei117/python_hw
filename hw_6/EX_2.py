"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта
для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна. Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class RoadOne:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_of_asphalt(self):
        the_mass_of_asphalt_in_one_square_meter_with_a_thickness_of_one_centimeter = 25
        thickness = 1
        return int(self._length * self._width *
                   the_mass_of_asphalt_in_one_square_meter_with_a_thickness_of_one_centimeter * thickness / 1000)


class RoadTow:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_of_asphalt(self):
        the_mass_of_asphalt_in_one_square_meter_with_a_thickness_of_one_centimeter = int(input('Введите массу асфальта '
                                                    'для покрытия одного кв метра дороги асфальтом, толщиной в 1 см: '))
        thickness = int(input('Введите толщину полотна в см.: '))
        return int(self._length * self._width *
                   the_mass_of_asphalt_in_one_square_meter_with_a_thickness_of_one_centimeter * thickness / 1000)


road_one = RoadOne(20, 5000)
print(road_one.weight_of_asphalt())

road_two = RoadTow(20, 5000)
print(road_two.weight_of_asphalt())
