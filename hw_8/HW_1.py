"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def method_one(cls, data):
        day, month, year = map(int, data.split('.'))
        return f'{day:02}.{month:02}.{year}'

    @staticmethod
    def method_two(data):
        day, month, year = map(int, data.split('.'))
        if day <= 1 or day >= 31:
            print('Вы ввели несуществующий дату')
        elif month <= 1 or month >= 12:
            print('Вы ввели несуществующий месяц')
        elif year < 0:
            print('Вы ввели несуществующий год')
        else:
            print(f'{day:02}.{month:02}.{year}')


print(Data.method_one('02.03.2021'))

my_class = Data('03.03.2021')
print(my_class.method_one('03.03.2021'))

Data.method_two('00.03.2021')
Data.method_two('04.00.2021')
Data.method_two('04.03.-2021')
Data.method_two('04.03.2021')
