# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

def my_func(number_one, number_two, number_tree):
    return number_one + number_two + number_tree - min(number_one, number_two, number_tree)


input_user_one = int(input('Введите первое число: '))
input_user_two = int(input('Введите второе число: '))
input_user_tree = int(input('Введите третье число: '))

print(f'Сумма двух наибольших чисел равна: {my_func(input_user_one, input_user_two, input_user_tree)}')
