import random
import math

################## 1 ################################### рек. ф-я степени числа

def st(a,n):
    if n == 1:
        return a
    elif n == 0:
        return 1
    else:
        return a * st(a,n-1)
a = int(input('Введите число: '))
n = int(input('Введите степень: '))
print(st(a,n))

################## 2 ############################## рекю ф-я суммы чисел в диапазоне

def sum(a,b):
    if a == b:
        return a
    else:
        s = 0
        for i in range(a,b):
            s+=i
        return a+sum(a+1,b)
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print('Сумма чисел',sum(a,b))

############ 3 ############################## рек. ф-я ,звездочки в ряд

def zn(n):
    if n == 1:
        return '*'
    else:
        s = '*'
        return s+ str(zn(n-1))
n = int(input('Введите число: '))
print(zn(n))

########### 4 ######################### крестики-нолики

def print_list (list_position):
    print('-------------')
    for i in range(3):
        print('|',list_position[0+i*3],'|',list_position[1+i*3],'|',list_position[2+i*3],'|')
        print('-------------')

def take_input(player_token,list_position):   # Ход игрока
    valTrue = False
    while not valTrue:
        try:
            player_answer = int(input('Куда будем ставить'+ player_token + '?\nВведите значение от 0 до 8: '))
        except:
            print('Некорректный ввод. Число от 0 до 8')
            continue
        if player_answer >= 0 and player_answer <= 8:
            if (str(list_position[player_answer])) not in "x0":
                list_position[player_answer] = player_token
                valTrue = True
            else:
                print('Клетка уже занята')
        else:
            print('Неправильный ввод числа. Число от 0 до 8')

def win(list_position):  # Условие победы
    win_list = ( (0,1,2),(0,3,6),(0,4,8),(1,4,7),(2,5,8),(2,4,6),(3,4,5),(6,7,8))
    for i in win_list:
        if list_position[i[0]] == list_position[i[1]] == list_position[i[2]] and list_position[i[2]]!='0':
            return list_position[i[0]]
    return  False


list_position = [' ',' ',' ',' ',' ',' ',' ',' ',' ']


player_token = 'x'
# print_list(list_position)
counter = 0
win_check = False

while not win_check:
    print_list(list_position)
    if counter %2 == 0:
        take_input('x',list_position)
    else:
        take_input('0',list_position)
    counter+=1
    if counter > 4 :
        value_win = win(list_position)
        if value_win:
            print('Выиграл игрок -', value_win)
            win_check = True
            break
    if counter == 9:
        print(' Победителя нет - Ничья')
        break
print_list(list_position)


####################### 5 ################################ Индекс, с которого начинается минимальная последовательность

a = [i for i in random.sample(range(0,100),100)]
print(a)

def min(a):
    start = 0
    if start > len(a) - 10:
        return None
    else:
        min_s = sum(a[start:start+10])
        min_i = start
        for i in range(start+1, len(a)-10):
            s = sum(a[i:i+10])
            if s < min_s:
                min_s = s
                min_i = i
    print('Индекс, с которого начинается минимальная последовательность: [',min_i,']')
min(a)

###################### 6 ######################## даты

def visoc(y1):
    if y1%400 == 0 or y1%4 == 0 and y1%100 != 0:
        return True
    else:
        return False

def day(y1,m1,d1,y2,m2,d2):

    visoc(y1)

    if visoc(y1) == False:
        year = [31, 28,31,30,31,30,31,31,31,30,31,30,31]
    else:
        year = [31, 29,31,30,31,30,31,31,31,30,31,30,31]

    #количество високосных и невисокосных лет от нулевого до y1
    yvis1 = 0
    ynonvis1 = 0
    for i in range(y1-1):
        if i % 400 == 0 or i % 4 == 0 and i % 100 != 0:
            yvis1 += 1
        else:
            ynonvis1 += 1
    # количество високосных и невисокосных лет от нулевого до y2
    yvis2 = 0
    ynonvis2 = 0
    for i in range(y2-1):
        if i % 400 == 0 or i % 4 == 0 and i % 100 != 0:
            yvis2 += 1
        else:
            ynonvis2 += 1
    # количество дней от 1 января 0 года до наших дат
    num1 = yvis1*366 + ynonvis1*365 + sum(year[0:m1 - 1]) + d1
    num2 = yvis2*366 + ynonvis2*365 + sum(year[0:m2 - 1]) + d2

    print('Между датами', abs(num2 - num1), 'дней.')

try:
    y1 = int(input('Введите год первой даты: '))
    m1 = int(input('Введите номер месяца первой даты: '))
    d1 = int(input('Введите день первой даты: '))
    y2 = int(input('Введите год второй даты: '))
    m2 = int(input('Введите  номер месяца второй даты: '))
    d2 = int(input('Введите день второй даты: '))
except:
    print('Введите корректно даты.')

day(y1,m1,d1,y2,m2,d2)











