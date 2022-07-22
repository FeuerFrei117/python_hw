"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number


one = ComplexNumber(complex(1, 2))
print(one.number)

two = ComplexNumber(complex(2, 3))
print(two.number)

print(one + two)
print(one * two)
