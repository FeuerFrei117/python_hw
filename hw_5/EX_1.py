"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
ввода данных свидетельствует пустая строка.
"""

with open('text_for_ex_1.txt', 'w+', encoding='utf-8') as file:
    while True:
        user_input = input('Введите текст, который хотите сохранить, для выхода введите пустую строку: ')
        if user_input == '':
            break
        else:
            file.write(f'{user_input}\n')


"""Создал для тренировки и проверки записаннового в файле"""
with open('text_for_ex_1.txt', encoding='utf-8') as file:
    new_file = file.read()
    print(new_file)
