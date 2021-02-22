"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income
(доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position реализовать
методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу
примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать
методы экземпляров).
"""


class Worker:

    def __init__(self):
        self.name = input('Введите свое имя: ')
        self.surname = input('Введите свою фамилию: ')
        self.position = input('Введите свою должность: ')
        self._income = {
            'wage': int(input('Введите оклад: ')),
            'bonus': int(input('Введите премию: '))
        }


class Position(Worker):

    def get_full_name(self):
        return print(f'Имя: {self.name}; Фамилия: {self.surname}')

    def get_total_income(self):
        income = self._income['wage'] + self._income['bonus']
        return print(f'Доход с учетом премии: {income}')


worker_one = Position()
print(worker_one.name)
print(worker_one.surname)
print(worker_one.position)
print(worker_one._income['wage'])
print(worker_one._income['bonus'])

worker_one.get_full_name()
worker_one.get_total_income()
