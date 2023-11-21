numb = int(input('Введите номер квадрата(от 1 до 10),который необходимо вывести: '))

if numb == 1:
    string = ''
    for i in range(5):
        for j in range(5):
            if i <= j:
                string += '*'
            else:
                string += '0'
        string += '\n'
    print(string)

elif numb == 2:
    string = ''
    for i in range(5):
        for j in range(5):
            if i >= j:
                string += '*'
            else:
                string += '0'
        string += '\n'
    print(string)

elif numb == 3:
    string = ''
    for i in range(5):
        for j in range(5):
            if i <= j and i < 5 - j:
                string += '*'
            else:
                string += '0'
        string += '\n'
    print(string)

elif numb == 4:
    string = ''
    for i in range(5):
        for j in range(5):
            if i >= j and i >= 5 - j - 1:
                string += '*'
            else:
                string += '0'
        string += '\n'
    print(string)

elif numb == 5:
    string = ''
    for i in range(5):
        for j in range(5):
            if i <=j and i<5-j:
                string+='*'
            elif i >= j and i >= 5-j-1:
                string += '*'
            else:
                string+='0'
        string+='\n'
    print(string)

elif numb == 6:
    string = ''
    for i in range(5):
        for j in range(5):
            if j <=5-i-1 and i>=j:
                string+='*'
            elif  j >=5-i-1 and i<=j:
                string += '*'
            else:
                string+='0'
        string+='\n'
    print(string)

elif numb == 7:
    string = ''
    for i in range(5):
        for j in range(5):
            if j <=5-i-1 and i>=j:
                string+='*'
            else:
                string+='0'
        string+='\n'
    print(string)

elif numb == 8:
    string = ''
    for i in range(5):
        for j in range(5):
            if j >=5-i-1 and i<=j:
                string+='*'
            else:
                string+='0'
        string+='\n'
    print(string)

elif numb == 9:
    string = ''
    for i in range(5):
        for j in range(5):
            if j <=5-i-1:
                string+='*'
            else:
                string+='0'
        string+='\n'
    print(string)

elif numb == 10:
    string = ''
    for i in range(5):
        for j in range(5):
            if j >=5-i-1:
                string+='*'
            else:
                string+='0'
        string+='\n'
    print(string)

else:
    print('Введите корректный номер.')







