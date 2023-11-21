#
# import math
#
#
# #################### 1- 2 #################################
#
#
#
#
# class Shape():
#     def __init__(self,name):
#         self.name = name
#
#     def __str__(self):
#         return f"Название: {self.name}\n"
#
#
# class Rectangle(Shape): # S = a*b
#     def __init__(self, a,b):
#         super().__init__("Прямоугольник")
#         self.a = a
#         self.b = b
#
#     def square(self):
#         return self.a * self.b
#
#     def __int__(self):
#         return int(Rectangle.square(self))
#
#     def __str__(self):
#         return (f"Имя фигуры:{self.name}\n Площадь: {Rectangle.__int__(self)}")
#
#
# class Circle(Shape): # S = Pi *r **2
#     def __init__(self, radius):
#         super().__init__("Круг")
#         self.radius = radius
#
#     def square(self):
#         return (self.radius ** 2) + math.pi
#
#     def __int__(self):
#         return int(Circle.square(self))
#
#     def __str__(self):
#         return (f"Имя фигуры:{self.name}\n Площадь: {Circle.__int__(self)}")
#
#
# class Right_triangle(Shape):  # S = 1/2bh
#     def __init__(self, b, h):
#         super().__init__("Прямоугольный треугольник")
#         self.b = b
#         self.h = h
#
#     def square(self):
#         return 1 / 2 * self.h * self.b
#
#     def __int__(self):
#         return int(Right_triangle.square(self))
#
#     def __str__(self):
#         return (f"Имя фигуры:{self.name}\n Площадь: {Right_triangle.__int__(self)}")
#
#
# class Trapezoid(Shape):
#     def __init__(self, a, b, h):
#         super().__init__("Трапеция")
#         self.a = a
#         self.b = b
#         self.h = h
#
#     def square(self):
#         return 1 / 2 * self.h * (self.b + self.a)
#
#     def __int__(self):
#         return int(Trapezoid.square(self))
#
#     def __str__(self):
#         return (f"Имя фигуры:{self.name}\n Площадь: {Trapezoid.__int__(self)}")
#
#
# rect = Rectangle(2, 5)
# circle = Circle(60)
# rt = Right_triangle(5, 10)
# trape = Trapezoid(2, 5, 10)
#
# for class1 in (rect, circle, rt, trape):
#     print("*" * 11)
#     print(f"{class1}")


##################### 3 #############################

class Shape:
    def __init__(self, name):
        self.name = name

    def Show(self):
        return f"Фигура: {self.name}"

    def Save(self):
        with open("shape.txt", "a", encoding="utf-8") as file:
            file.write(self.Show())

    def Load(self):
        with open("shape.txt", "r", encoding="utf-8") as file:
            return file.read()


class Square(Shape):
    def __init__(self, x, y, lenth):
        super().__init__("Квадрат")
        self.x = x
        self.y = y
        self.lenth = lenth

    def Show(self):
        return f"Фигура: {self.name}\nКоординаты угла: ({self.x},{self.y})\nДлина стороны: {self.lenth}\n\n"


class Rectangle(Shape):
    def __init__(self, x, y, a, b):
        super().__init__("Прямоугольник")
        self.x = x
        self.y = y
        self.a = a
        self.b = b

    def Show(self):
        return f"Фигура: {self.name}\nКоординаты угла: ({self.x},{self.y})\nДлина сторон: {self.a} : {self.b}\n\n"


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__("Окружность")
        self.x = x
        self.y = y
        self.radius = radius

    def Show(self):
        return f"Фигура: {self.name}\nКоординаты центра: ({self.x},{self.y})\nРадиус: {self.radius}\n\n"


class Ellipse(Shape):
    def __init__(self, x, y, a, b):
        super().__init__("Эллипс")
        self.x = x
        self.y = y
        self.a = a
        self.b = b

    def Show(self):
        return f"Фигура: {self.name}\nКоординаты угла: ({self.x},{self.y})\nДлина сторон: {self.a} : {self.b}\n\n"

# Результат
sq = Square(2, 3, 5)
rec = Rectangle(1, 2, 4, 6)
cir = Circle(0, 1, 10)
el = Ellipse(0, 0, 5, 9)

for i in (sq, rec, cir, el):
    i.Save()

print(sq.Load())

with open("shape.txt", "r", encoding="utf-8") as file:
    print(file.read())




# ЛИБО ЕЩЕ ВОТ ТАК, ДОПОЛНИТЕЛЬНЫЕ СПИСКИ

# figure = [Square(2, 3, 5),Rectangle(1, 2, 4, 6),Circle(0, 1, 10),Ellipse(0, 0, 5, 9)]
#
# for i in figure:
#     i.Save()
#
# spisok = []
# with open("shape.txt", "r", encoding="utf-8") as file:
#     for i in file.readlines():
#         if i !="\n":
#             spisok.append(i.strip())
# print(spisok)

