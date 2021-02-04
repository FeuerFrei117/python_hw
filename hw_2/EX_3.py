# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

user_input = input('Введите месяц в виде целого числа от 1 до 12: ')

season_1 = {
    '1': 'зима',
    '2': 'зима',
    '3': 'весна',
    '4': 'весна',
    '5': 'весна',
    '6': 'лето',
    '7': 'лето',
    '8': 'лето',
    '9': 'осень',
    '10': 'осень',
    '11': 'осень',
    '12': 'зима'
}
print(season_1[user_input])

season_2 = ['зима', 'весна', 'лето', 'осень']
if user_input == '12' or user_input == '1' or user_input == '2':
    print(season_2[0])
elif user_input == '3' or user_input == '4' or user_input == '5':
    print(season_2[1])
elif user_input == '6' or user_input == '7' or user_input == '8':
    print(season_2[2])
elif user_input == '9' or user_input == '10' or user_input == '11':
    print(season_2[3])
