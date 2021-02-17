"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран.
"""

"""Тренировлся в создании и записи в файл информации, основной код работет и без этого"""
# with open('text_for_ex_5.txt', 'w', encoding='utf-8') as file:
#     file.write(input('Введите любое колличество чисел, разделенных пробелами, для подсчета их суммы: '))

with open('text_for_ex_5.txt', 'r', encoding='utf-8') as file:
    entire_file = file.readlines()
    for one_line in entire_file:
        sum_number = 0
        for num in one_line.split():
            sum_number += int(num)
        print(sum_number)
