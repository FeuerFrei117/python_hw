"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json

info_list = [{}, {}]

with open('text_for_ex_7.txt', 'r', encoding='utf-8') as file:
    entire_file = file.readlines()
    average_profit = 0
    companies_with_profits = 0
    for one_line in entire_file:
        info_about_company = one_line.split()
        average_profit_company = int(info_about_company[2]) - int(info_about_company[3])
        info_list[0][info_about_company[0]] = average_profit_company
        if average_profit_company >= 0:
            average_profit += average_profit_company
            companies_with_profits += 1
    info_list[1]['average_profit'] = int(average_profit / companies_with_profits)
print(info_list)

with open('text_for_ex_7.json', 'w', encoding='utf-8') as file:
    json.dump(info_list, file)

"""Сделал десерилизацию файла, который Вы нам отправляли"""

with open('text_77.json', 'r', encoding='utf-8') as file:
    new_file = json.load(file)

print(new_file)
print(type(new_file))
