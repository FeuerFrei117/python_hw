"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто
из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
сотрудников.
"""

with open('text_for_ex_3.txt', 'r', encoding='utf-8') as file:
    entire_file = file.readlines()
    average_income_of_employees = 0
    print('Сотрудники с окладом менее 20 тыс.:')
    for num, i in enumerate(entire_file, 1):
        if float(i.split()[1]) < 20000:
            print(i, end='')
        average_income_of_employees += float(i.split()[1])
    print(f'Средняя величина дохода сотрудников: {average_income_of_employees / num:.2f}')
