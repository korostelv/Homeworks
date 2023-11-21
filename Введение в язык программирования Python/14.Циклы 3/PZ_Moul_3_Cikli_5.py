##### Modul_3_5_
#################### 1 #########################3

# a = input('Введите число: ')
# i = 0
#
# for i in range(len(a)):
#     i+=1
#
# print(f'В числе {i} цифр')
# print('В числе',a.count('0'),'нулей')
#
# sum = 0
# for i in range(len(a)):
#     sum +=int(a[i])
# print('Сумма чисел: ',sum)
# print('Среднеарифметическое: ', sum/len(a))

####################### 2 ####################################

# a = int(input('Введите размер клетки :'))
# b = '*'*a + '-'*a
# c = '-'*a + '*'*a
# string = ''
# for i in range(8):
#     for j in range(4):
#         if i%2 == 0:
#             string += b
#         elif i%2 != 0:
#             string += c
#     string += '\n'
# print(string)


######################### 3 #####################33
# import  random
#
# level = int(input('Введите уровень сложности от 1 до 3: '))
#
# count = 0
# i = 0
#
# if level == 1:
#     while(count<5):
#         x = random.randint(2, 5)
#         y = random.randint(2, 9)
#         count+=1
#         z = x*y
#         print(f'{x} * {y} =')
#         z1 = int(input())
#         if z == z1:
#             i+=1
#             print('Ответ правильный')
#         else:
#             print('Ответ не правильный')
# elif level == 2:
#     while(count<10):
#         x = random.randint(5, 9)
#         y = random.randint(5, 9)
#         count+=1
#         z = x*y
#         print(f'{x} * {y} =')
#         z1 = int(input())
#         if z == z1:
#             i+=1
#             print('Ответ правильный')
#         else:
#             print('Ответ не правильный')
# elif level == 3:
#     while (count < 10):
#         x = random.randint(2, 9)
#         y = random.randint(11, 19)
#         count += 1
#         z = x * y
#         print(f'{x} * {y} =')
#         z1 = int(input())
#         if z == z1:
#             i += 1
#             print('Ответ правильный')
#         else:
#             print('Ответ не правильный')
#
#
# print('Правильных ответов', i ,'из',count )
# if i/count <= 1 and i/count > 0.8:
#         print('Оценка: 5')
# elif i/count <= 0.8 and i/count > 0.6:
#         print('Оценка: 4')
# elif i/count <= 0.6 and i/count > 0.4:
#         print('Оценка: 3')
# elif i/count <= 0.4 and i/count > 0.2:
#         print('Оценка: 2')
# else:
#         print('Оценка: 1')


##################### 4 ###########################

# n = 8
#
# string = ''
# for i in range(n):
#     for j in range(n):
#         if i >= n/2 and j >= n/2 :
#             string+= ''
#
#         else:
#             string+= '*'
#
#
#     string += '\n'
#
# print(string.center(8,'-'))

n=int(input("enter the no of rows :"))
for i in range(0,n+1):
    for j in range(0,n-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
# if i==n:
#     for i in range(n-1,0,-1):
#         for j in range(0,n-i):
#             print(end=" ")
#         for j in range(0,i):
#             print("*",end=" ")
#         print()