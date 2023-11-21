import random

pole = [str(i).rjust(2,' ')  for i  in random.sample(range(16),16)]

def list_pole(pole):
    print('_' * 21)
    for i in range(4):
        print('|', pole[0 + i * 4], '|', pole[1 + i * 4], '|', pole[2 + i * 4], '|', pole[3 + i * 4], '|')
        print('-' * 21)


def game():

    list_pole(pole)
    count = 0

    while pole != sorted(pole):
        index_null = pole.index(' 0')
        # try:
        #     sdvig = input('Выберите куда будете сдвигать Ноль: \nW - вверх\nA - влево\nS - вниз\nD - вправо\n:')
        # except:
        #    print('Активны только клавиши WASD')
        #    continue

        sdvig = input('Выберите куда будете сдвигать Ноль: \nW - вверх\nA - влево\nS - вниз\nD - вправо\n:')

        if sdvig == 'w':
            if index_null == 0 or index_null == 1 or index_null == 2 or index_null == 3:
                print('Верхний край поля')
                list_pole(pole)
            else:
                pole[index_null], pole[index_null - 4] = pole[index_null - 4], pole[index_null]
                count += 1
                list_pole(pole)
        elif sdvig == 'a':
            if index_null == 0 or index_null == 4 or index_null == 8 or index_null == 12:
                print('Левый край поля')
                list_pole(pole)
            else:
                pole[index_null], pole[index_null - 1] = pole[index_null - 1], pole[index_null]
                count += 1
                list_pole(pole)
        elif sdvig == 's':
            if index_null == 12 or index_null == 13 or index_null == 14 or index_null == 15:
                print('Нижний край поля')
                list_pole(pole)
            else:
                pole[index_null], pole[index_null + 4] = pole[index_null + 4], pole[index_null]
                count += 1
                list_pole(pole)
        elif sdvig == 'd':
            if index_null == 3 or index_null == 7 or index_null == 11 or index_null == 15:
                print('Верхний край поля')
                list_pole(pole)
            else:
                pole[index_null], pole[index_null + 1] = pole[index_null + 1], pole[index_null]
                count += 1
                list_pole(pole)
        else:
            print('Активны только клавиши WASD')

        print('Количество ходов: ', count)


game()