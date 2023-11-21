
################### 1 ############ Singleton
#
# class Singleton:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#
# a = Singleton()
# b = Singleton()
# # print(a)
# # print(b)
#
#
#
# ############### 2 ###################### Abstract fabric
#
#
# from decimal import *
#
# class Factory(object):
#     def build_sequence(self): #Для работы со всеми типами данных
#         return []
#     def build_number(self,string): #для работы с числами
#         return Decimal(string)
#
# class Loader(object):
#     def Load(string, factory):
#         sequence = factory.build_sequence()
#         for substring in string.split(","):
#             item = factory.build_number(substring)
#             sequence.append(item)
#         return sequence
#
#
# f = Factory()
# result = Loader.Load('1.23,4.56',f)
# # print(result)


############## 3 #########################


class Loader():
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, numb):
        self.numb = numb

    def __str__(self):
        return f"{self.numb}\nМаксимум: {str(max(self.numb))}\nМинимум: {str(min(self.numb))}"

    def write(self):
        path = input("Введите путь и название файла: ")
        with open(path, "a", encoding="utf-8") as file:
            file.write(str(self.numb))
            file.write("\nМаксимум: ")
            file.write(str(max(self.numb)))
            file.write("\nМинимум: ")
            file.write(str(min(self.numb)))




num = input("Введите числа через пробел: ").split()
numb =[]
for i in num:
    i = int(i)
    numb.append(int(i))
a = Loader(numb)

s = int(input("Хотите вывести или записать значение в файл? -->(1-вывод, 2-запись): "))
if s == 1:  # для записи
    print(a)
elif s == 2:  # для вывода
    a.write()
else:
    print("Выход")