"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых
пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой.
"""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


number_one = input('Введите делимое: ')
number_two = input('Введите делитель: ')

try:
    if int(number_two) == 0:
        raise OwnError('На ноль делить нельзя!')
    result = int(number_one) / int(number_two)
except OwnError as arr:
    print(arr)
except ValueError:
    print('Вы ввели текст')
else:
    print(f'Результат: {int(result)}')
