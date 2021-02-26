"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух
матриц). Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""

from copy import deepcopy


class Matrix:

    def __init__(self, user_list):
        self.user_list = user_list
        self.number_sum = deepcopy(self.user_list)

    def __str__(self):
        self.result = ''
        for i in self.user_list:
            for b in i:
                self.result += str(f'{b} ')
            self.result += '\n'
        return self.result

    def __add__(self, other):
        for num_one, i in enumerate(other.user_list):
            for num_two, t in enumerate(i):
                self.number_sum[num_one][num_two] += t
        return self


matrix_1 = Matrix([[1, 1], [2, 2]])
print(matrix_1)

matrix_2 = Matrix([[3, 3], [4, 4]])
print(matrix_2)

matrix_3 = Matrix([[5, 5], [6, 6]])
print(matrix_3)

matrix_1 + matrix_2 + matrix_3
print(matrix_1.number_sum)
"""Проверял, изменяется ли matrix_1.user_list после сложения"""
print(matrix_1.user_list)
