"""
Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения
до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод
позволяет организовать ячейки по рядам.

Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n**.

Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n*****.
"""


class Cell:
    def __init__(self, cell_count):
        self.cell_count = int(cell_count)

    def __add__(self, number):
        self.cell_count += int(number)

    def __sub__(self, number):
        result = self.cell_count - int(number)
        if result >= 0:
            self.cell_count = result
        else:
            print('Отрицательного количества клеток не может быть!')

    def __mul__(self, number):
        result = self.cell_count * int(number)
        if result > 0:
            self.cell_count = result
        else:
            print('Умножать на 0 или отрицательное число нельзя!')

    def __truediv__(self, number):
        try:
            integer_number = self.cell_count / int(number)
            if integer_number > 0:
                self.cell_count = int(integer_number)
            else:
                print('Делить на отрицательное число нельзя!')
        except ZeroDivisionError:
            print('Делить на 0 нельзя!')

    def make_order(self, number_of_cells_in_a_row):
        super().__init__()
        number = self.cell_count
        num = 0
        for i in range(number):
            if num < number_of_cells_in_a_row:
                print('*', end='')
                num += 1
            else:
                print('\\n*', end='')
                num = 1


cell_one = Cell(5)
cell_one + 8
print(cell_one.cell_count)

cell_one - 1
print(cell_one.cell_count)

cell_one * 2
print(cell_one.cell_count)

cell_one / 2
print(cell_one.cell_count)

cell_one.make_order(5)
