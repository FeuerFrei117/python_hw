# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user = int(input('Введите время в секундах: '))

''' Первый вариант решения'''
hour = 0
minutes = 0
seconds = user % 60

while user >= 60:
    user -= 60
    minutes += 1
    if minutes == 60:
        minutes -= 60
        hour += 1


'''Второй вариант'''
# hour = user // 3600
# seconds = user % 60
# minutes = int((user - seconds - (hour * 3600)) / 60)

print(f'{hour}:{minutes}:{seconds}')
