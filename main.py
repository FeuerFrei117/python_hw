# n, m, k = (int(i) for i in input().split())  # чтение размеров поля и числа мин
# a = [[0 for j in range(m)] for i in range(n)]  # заполнение поля нулями
# for i in range(k):
#     row, col = (int(i) - 1 for i in input().split())
#     a[row][col] = -1  # расставляем мины
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == 0:  # в этой клетке мины нет, поэтому считаем число мин вокруг
#             for di in range(-1, 2):
#                 for dj in range(-1, 2):
#                     ai = i + di
#                     aj = j + dj
#                     # (ai, aj)
#                     if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
#                         a[i][j] += 1
# # вывод результата
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == -1:
#             print('*', end='')
#         elif a[i][j] == 0:
#             print('.', end='')
#         else:
#             print(a[i][j], end='')
#     print()

# my_list = []
#
# while True:
#     my_list.append(int(input()))
#     if sum(my_list) == 0:
#         break
#
# print(sum(i ** 2 for i in my_list))


# user_input = int(input())
# len_homes = list(map(int, input().split()))

# total_students = int(input())
# coordinates_of_houses = list(map(int, input().split()))
#
# average = abs(abs(coordinates_of_houses[-1]) - sum(list(abs(i) for i in (coordinates_of_houses[:-1]))))
# coordinates = 0
#
# if abs(abs(coordinates_of_houses[-1]) - sum(list(abs(i) for i in (coordinates_of_houses[:-1])))) == 0:
#     coordinates = coordinates_of_houses[-1]
#     average = abs(abs(coordinates_of_houses[-1]) - sum(list(abs(i) for i in (coordinates_of_houses[:-1]))))
#
# if abs(abs(coordinates_of_houses[0]) - sum(list(abs(i) for i in (coordinates_of_houses[1:])))) == 0:
#     coordinates = coordinates_of_houses[0]
#     average = abs(abs(coordinates_of_houses[0]) - sum(list(abs(i) for i in (coordinates_of_houses[1:]))))
#
# for i in range(1, total_students-1):
#     left = sum(list(abs(i) for i in coordinates_of_houses[:i]))
#     right = sum(list(abs(i) for i in coordinates_of_houses[i+1:]))
#     if abs(left - right) <= average:
#         average = abs(left - right)
#         coordinates = coordinates_of_houses[i]
#
# print(coordinates)

# f_obj = open("my_DZ_5", 'w+', encoding='utf-8')
# f_obj.write("And I think it's gonna be a long long time"
#     "\nTill touch down brings me round again to find"
#     "\nI'm not the man they think I am at home"
#     "\nOh no no no I'm a rocket man, rocket man"
#     "\nBurning out his fuse up here alone")
# content = f_obj.read()
# print(content)

# f_obj = open("my_DZ_5", "w+", encoding="utf-8")
# f_obj.write("And I think it's gonna be a long long time\n"
#     "Till touch down brings me round again to find\n"
#     "I'm not the man they think I am at home\n"
#     "Oh no no no I'm a rocket man, rocket man\n"
#     "Burning out his fuse up here alone")
# content = f_obj.read()
# print(content)
# f_obj.close()
# f_obj = open("my_DZ_5", "r", encoding="utf-8")
# content = f_obj.read()
# print(content)

# with open('my_DZ_5', 'w+', encoding='utf-8') as file:
#     file.write("And I think it's gonna be a long long time"
#     "\nTill touch down brings me round again to find"
#     "\nI'm not the man they think I am at home"
#     "\nOh no no no I'm a rocket man, rocket man"
#     "\nBurning out his fuse up here alone")
#     for line in file:
#         print(line)
#
# with open('my_DZ_5', 'r', encoding='utf-8') as file:
#     print(file.read())

