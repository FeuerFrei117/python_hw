"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

"""Сильно заморочился, но вроде красиво получилось"""

my_dictionary = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре'
}

with open('text_for_ex_4.txt', 'r', encoding='utf-8') as file_1:
    entire_file = file_1.readlines()
    with open('result_text_for_ex_4.txt', 'w', encoding='utf-8') as file_2:
        for i in entire_file:
            # print(f'{my_dictionary[i.split()[0].lower()].capitalize()} {" ".join(i.split()[1:])}')
            file_2.write(f'{my_dictionary[i.split()[0].lower()].capitalize()} {" ".join(i.split()[1:])}\n')
