"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут
реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на
ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый,
зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""
from time import sleep
from itertools import cycle


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        """Решение № 1"""
        # while True:
        #     print(f'\033[31m{TrafficLight.__color[0]}')
        #     sleep(7)
        #     print(f'\033[33m{TrafficLight.__color[1]}')
        #     sleep(2)
        #     print(f'\033[32m{TrafficLight.__color[2]}')
        #     sleep(10)
        """Решение № 2"""
        # for i in cycle(TrafficLight.__color):
        #     if i == 'red':
        #         print(i)
        #         sleep(7)
        #     elif i == 'yellow':
        #         print(i)
        #         sleep(2)
        #     else:
        #         print(i)
        #         sleep(10)


traffic_light = TrafficLight()
traffic_light.running()

