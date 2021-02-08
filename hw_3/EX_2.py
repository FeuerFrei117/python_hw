# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.

def print_user_info(name, surname, year_of_birth, city_of_living, email, tel):
    print(f'Имя: {name}, Фамили: {surname}, Год рождения: {year_of_birth}, Город проживания: {city_of_living}, '
          f'email: {email}, телефон: {tel}')


print_user_info(name=input('Введите имя: '), surname=input('Введите фамилию: '), year_of_birth=input('Введите год '
                'рождения: '), city_of_living=input('Введите город проживания: '), email=input('Введите email: '),
                tel=input('Введите номер телефона: '))
