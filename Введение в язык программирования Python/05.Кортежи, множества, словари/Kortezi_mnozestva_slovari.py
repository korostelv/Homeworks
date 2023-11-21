############ 1 ################### Баскетболисты

bulls = {"Michael Jordan":198, "Magic Johnson":206, "Dennis Rodman":201}
print(bulls)
a = int(input('Введите\n1 - Чтобы добавить игрока\n2 - Чтобы удалить игрока\n3 - Чтобы получить информацию о игроке\n4 - Чтобы заменить игрока\n: '))
if a == 1:
    name = input('Введите имя игрока: ')
    height = int(input('Введите рост игрока: '))
    bulls[name] = height
    print(bulls)
elif a == 2:
    name = input('Введите имя удаляемого игрока: ')
    bulls.pop(name)
    print(bulls)
elif a == 3:
    name = bulls[input('Введите имя игрока: ')]
    print('Рост игрока: ',name,'см.')
elif a == 4:
    name = input('Введите имя игрока: ')
    height = int(input('Измените рост игрока: '))
    bulls[name] = height
    print(bulls)

############### 2 ####################### Англ-франц

d = {"home":"domicile",
     "hand":"main",
     "cat":"chat",
     "dog":"chien"}
print(d)

a = int(input('Введите\n1 - Чтобы добавить слово\n2 - Чтобы удалить слово\n3 - Чтобы найти слово\n4 - Чтобы заменить перевод слова\n: '))

if a == 1:
    word = input('Введите новое слово: ')
    trans = input('Введите перевод слова на французский: ')
    d[word] = trans
    print(d)
elif a == 2:
    word = input('ВВедите удаляемое слово: ')
    d.pop(word)
    print(d)
elif a == 3:
    word = d[input('Введите нужное слово: ')]
    print('По-французски это',word)
elif a == 4:
    word = input('Введите слово: ')
    new_trans = input('Введите новый перевод: ')
    d[word] = new_trans
    print(d)

#################### 3 ####################### Фирма

firm = {
    "Иванов":{"name":"Иван", "surname":"Иваныч", "tel":8342121316, "job":"Директор", "office":1, "skype":"sk_ivanov"},
    "Петров":{"name":"Петр", "surname":"Петрович", "tel":8342147255, "job":"Админ", "office":2, "skype":"sk_petrov"},
    "Сидоров":{"name":"Сидор", "surname":"Сидорыч", "tel":8342789456, "job":"Бухгалтер", "office":3, "skype":"sk_sidorov"}
}
print(firm)

a = int(input('Введите\n1 - Чтобы добавить сотрудника\n2 - Чтобы удалить сотрудника или его данные\n3 - Чтобы найти информацию о сотруднике\n4 - Чтобы изменить данные о сотруднике\n: '))

if a == 1:
    worker = dict.fromkeys([input('Введите фамилию нового сотрудника: ')])
    worker["name"] = input('Введите имя: ')
    worker["surname"] = input('Введите отчество: ')
    worker["tel"] = int(input('Введите номер телефона: '))
    worker["job"] = input('Введите должность: ')
    worker["office"] = int(input('Введите номер кабинета: '))
    worker["skype"] = input('Введите Skype: ')
    firm.update(worker)
    print(firm)
if a == 2:
    b = int(input('Введите\n1 - Чтобы удалить сотрудника\n2 - Чтобы удалить отдельные данные сотрудника\n: '))
    if b == 1:
        worker = input('Введите фамилию удаляемого сотрудника: ')
        firm.pop(worker)
        print(firm)
    elif b == 2:
        user = firm[input("Введите фамилию сотрудника: ")]
        file = input('Введите удаляемые данные: ')
        user.pop(file)
        print(firm)
if a == 3:
    worker = input('Введите фамилию сотрудника: ')
    for i in firm:
            for k,v in firm[i].items():
                if i == worker:
                    print(k,':',v)
if a == 4:
    user = firm[input("Введите фамилию сотрудника: ")]
    file = input('Введите изменяемые данные: ')
    user[file] = input('Введите значение данных: ')
    print(firm)








