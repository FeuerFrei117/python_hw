# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user = int(input('Введите целое положительное число: '))
biggest_number = 0

while user >= 1:
    last_number = int(user % 10)
    if last_number == 9:
        print('Самая большая цифра в вашем числе: 9')
        break
    elif last_number > biggest_number:
        biggest_number = last_number
    user /= 10
else:
    print(f'Самая большая цифра в вашем числе: {biggest_number}')
