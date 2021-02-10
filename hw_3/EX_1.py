# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

def division_of_two_numbers(number_one, number_two):
    try:
        result = number_one / number_two
        print(result)
    except ZeroDivisionError:
        print('Деление на "0!"')


input_user_number_one = int(input('Введите первое число: '))
input_user_number_two = int(input('Введите второе число: '))

division_of_two_numbers(input_user_number_one, input_user_number_two)
