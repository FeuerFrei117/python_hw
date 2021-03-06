# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
# программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
# чисел к полученной ранее сумме и после этого завершить программу.

user_input_sum = 0
condition = True
while condition:
    user_input = input('Введите строку чисел, разделенных пробелами.\n'
                       'Для выхода введите "q": ').lower()
    for i in user_input.split():
        if i == 'q':
            condition = False
            break
        else:
            user_input_sum += int(i)
    print(f'Сумма введеных вами чисел равна: {user_input_sum}')

