"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества
слов в каждой строке.
"""

"""Решение № 1"""
with open('text_for_ex_2.txt', 'r') as file:
    line_number = 1
    while True:
        one_line = file.readline()
        if one_line == '':
            break
        else:
            print(f'Строка № {line_number}, слов в строке: {len(one_line.split())}')
            line_number += 1

"""Решение № 2"""
with open('text_for_ex_2.txt', 'r') as file:
    line_number = 1
    entire_file = file.readlines()
    for i in entire_file:
        print(f'Строка № {line_number}, слов в строке: {len(i.split())}')
        line_number += 1
