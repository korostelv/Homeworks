########### 1 ###################
import  math

class Square:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Название фигуры: {self.name}"


class Cirсle(Square):
    def __init__(self, a):
        super().__init__("Вписанная окружность")
        self.a = a

    def __str__(self):
        return f"Название фигуры: {self.name}\nРадиус вписанной окружности: {self.a / 2}\nДлина окружности:{2 * math.pi * (self.a / 2)} "


c = Cirсle(5)
print(c)

########## 2 ################

class Animal:
    def __init__(self):
        self.kind = "Animal"
        self.sound = ""
        self.name = ""
        self.type = ""

    def Sound(self):
        return f"Говорит {self.sound}"

    def Show(self):
        return f"Зовут {self.name}"

    def Type(self):
        return f"Порода {self.type}"


class Dog(Animal):
    def __init__(self):
        self.kind = "Dog"
        self.sound = "гав"
        self.name = "Шарик"
        self.type = "Дворняга"


class Cat(Animal):
    def __init__(self):
        self.kind = "Cat"
        self.sound = "мяу"
        self.name = "Мурзик"
        self.type = "Сибирская"


class Parrot(Animal):
    def __init__(self):
        self.kind = "Parrot"
        self.sound = "аррр"
        self.name = "Дурик"
        self.type = "Ара"


class Hamster(Animal):
    def __init__(self):
        self.kind = "Hamster"
        self.sound = "фрфр"
        self.name = "Хома"
        self.type = "Джунгарик"


cat = Cat()
dog = Dog()
ham = Hamster()
par = Parrot()

for i in [cat, dog, ham, par]:
    print("*" * 15)
    print(i.kind)
    print(i.Sound())
    print(i.Show())
    print(i.Type())

########### 2 ##############

class door:
    def __init__(self):
        self.namedoor = "passenger_door"
        self.material = "steel"
        self.color = "White"


class wheel:
    def __init__(self):
        self.namewheel = "sport_wheel"
        self.size = "x6"
        self.radius = "40cm"


class motor:
    def __init__(self):
        self.namemotor = "XPL_235A"
        self.powerhourse = "500"
        self.bulk = "120_l"


class control_box:
    def __init__(self):
        self.namebox = "1X2L_AAA_Class"
        self.speed = "6"
        self.drive = "all_wheel"


class Avto(door, wheel, motor, control_box):
    def __init__(self):
        control_box.__init__(self)
        motor.__init__(self)
        wheel.__init__(self)
        door.__init__(self)
        self.name = "BMW"

    def __str__(self, ):
        return f"Название {self.name}\n***************************\nКомплектация: \n\tКоробка передач - {self.namebox}\n\tСкорость - {self.speed}\n\tПривод -" \
               f" {self.drive}\n\tНазвание мотора - " \
               f"{self.namemotor}\n\tМощность - {self.powerhourse}\n\tОбъем - {self.bulk}\n\tНазвание колес - {self.namewheel}\n\tРадиус - {self.radius}\n\tРазмер - {self.size}\n\tНазвание " \
               f"дверей - {self.namedoor}\n\tМатериал - {self.material}\n\tЦвет - {self.color}"


avto = Avto()
print(avto)

############ 4-5 ####################

# class Employer:
#     def __init__(self):
#         self.name = "Employer"
#     def Print(self):
#         print( f" This is {self.name}")
#
#     def __str__(self):
#         return  f" This is {self.name} class"
#     def __int__(self):
#         return self.age
#
# class President(Employer):
#     def __init__(self):
#         self.name = "President"
#         self.salary = 150000
#         self.work = "Departament management"
#         self.age = 54
#     def Print(self):
#         print( f" This is {self.name}\nduties: {self.work}\nsalary: {self.salary}")
#
# class Manager(Employer):
#     def __init__(self):
#         self.name = "Manager"
#         self.salary = 45000
#         self.work = "Managing"
#         self.age = 18
#     def Print(self):
#         print( f" This is {self.name}\nduties: {self.work}\nsalary: {self.salary}")
#
# class Worker(Employer):
#     def __init__(self):
#         self.name = "Worker"
#         self.salary = 20000
#         self.work = "Transportation"
#         self.age = 41
#     def Print(self):
#         print( f" This is {self.name}\nduties: {self.work}\nsalary: {self.salary}")
#
#
#
# worker = Worker()
# manager = Manager()
# president = President()
#
# for i in [worker,manager,president]:
#     i.Print()
#     print(i)    #переопределение метода str
#     print(int(i))   #переопределение метода str
#     print("-"*20)




