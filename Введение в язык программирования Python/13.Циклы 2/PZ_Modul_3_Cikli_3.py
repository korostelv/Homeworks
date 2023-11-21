################## 1 ########################

# a = int(input('Введите число: '))
#
# i = 1
# while (i<= 9):
#     print(a, '*', i, '=', a * i)
#     i+=1

#################### 2 ########################


################## 3 #######################

# a = int(input('Введите нижнюю границу: '))
# b = int(input('Введите верхнюю границу: '))
# value = int(input('Введите число: '))
# string =[]
# while (value < a) or (value > b):
#     value = int(input('Введите число в диапазоне: '))
# for i in range(a, b + 1):
#     num = i
#     if i == value:
#         num = '!' + str(i) + '!'
#     if i == b:
#         print(num)
#     else:
#         print(num, end=' ')

#################### 4 #########################3
# import random
# import time
# import math
#
# x = random.randint(1, 500)
# # print(x)
# count = 0
# value = ''
# start = time.monotonic()
# while (value != x):
#     value = int(input('введите число: '))
#     count += 1
#     if value > x and value != 0:
#         print('Загаданное число меньше')
#     elif value < x and value != 0:
#         print('Загаданное число больше')
#     elif value == x:
#         print('Вы угадали!')
#     elif value == 0:
#         print('Выход')
#         break
# end = time.monotonic()
# print(f'Количество попыток {count}')
# print('Время', math.floor(end - start), 'c')