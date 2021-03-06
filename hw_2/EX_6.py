# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию
# об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками
# товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все
# данные у пользователя.
# Пример готовой структуры:
# [
# (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
# (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
# (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
# название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”, “шт.”, “шт.”]
# }
# *******************************************************************************************


products = []
i = 1
print('Добро пожаловать в программу "Структура данных"')
while input('Для продолжения работы нажмите "enter", для выхода введите "q": ').lower() != 'q':
    info_about_product = {
        'название': input('Введите название товара: '),
        'цена': input('Введите цену товара: '),
        'количество': input('Введите количество товара: '),
        'единица измерения': input('Введите единицу измерения товара: ')
    }
    products.append((i, info_about_product))
    i += 1

print(products)

print('*' * 100)

analytics = {}

for y in ['название', 'цена', 'количество', 'единица измерения']:
    b = 0
    my_list = []
    while b < i - 1:
        meaning = products[b][1].setdefault(y)
        my_list.append(meaning)
        b += 1
    analytics.update({y: my_list})
print(analytics)
