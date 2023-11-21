from abc import ABC, abstractmethod

class Toppings(ABC):
    @abstractmethod
    def add_cucumber(self):
        pass

    @abstractmethod
    def add_olives(self):
        pass

    @abstractmethod
    def add_onion(self):
        pass

    @abstractmethod
    def add_chili(self):
        pass

class Add_toppings(Toppings):
    def add_cucumber(self):
        print("Добавили корнишоны")

    def add_olives(self):
        print("Добавили оливки")

    def add_onion(self):
        print("Добавили лук")

    def add_chili(self):
        print("Добавили чили")

class Standart_pizza(Add_toppings):
    def __init__(self):
        self.four_cheeses = "Четыре сыра"
        self.hawai = "Гавайская"
        self.pepperoni = "Пепперони"
        self.carbonara = "Карбонара"
        self.vegan = "Вегетарианская"
        self.price_four_cheeses = 300
        self.price_hawai = 400
        self.price_pepperoni = 320
        self.price_carbonara = 350
        self.price_vegan = 280
        self.qt_four_cheeses = 0
        self.qt_hawai = 0
        self.qt_pepperoni = 0
        self.qt_carbonara = 0
        self.qt_vegan = 0
        self.full_price = 0
        self.chek = []
        self.statistika = ["Продажи: \n"]


class Menu(Standart_pizza):
    def __init__(self):
        super().__init__()
        
    def menu(self):
        print("Добро пожаловать в пиццерию!")
        self.chek.append("**********************\n")
        while True:
            value_pizza = input("Выберите пиццу:\n\t1 - Четыре сыра\n\t2 - Гавайская\n\t3 - Пепперони\n\t4 - Карбонара\n\t5 - Вегетарианская\n\t: ")
            if value_pizza == "1":
                print(f"Ваш выбор: {self.four_cheeses}")
                self.qt_four_cheeses += 1
                self.full_price += self.price_four_cheeses
                self.chek.append("Четыре сыра\n")
            elif value_pizza == "2":
                print(f"Ваш выбор {self.hawai}")
                self.qt_hawai += 1
                self.full_price += self.price_hawai
                self.chek.append("Гавайская\n")
            elif value_pizza == "3":
                print(f"Ваш выбор {self.pepperoni}")
                self.qt_pepperoni += 1
                self.full_price += self.price_pepperoni
                self.chek.append("Пепперони\n")
            elif value_pizza == "4":
                print(f"Ваш выбор {self.carbonara}")
                self.qt_carbonara += 1
                self.full_price += self.price_carbonara
                self.chek.append("Карбонара")
            elif value_pizza == "5":
                print(f"Ваш выбор {self.vegan}")
                self.qt_vegan += 1
                self.full_price += self.price_vegan
                self.chek.append("Вегетарианская\n")
            value_topping = input("Добавим топпинги(Y/N)?: ")
            if value_topping == "y":
                value = input("Добавим корнишоны(Y/N)?: ")
                if value == "y":
                    pizza.add_cucumber()
                    self.chek.append("\tКорнишоны\n")
                else:
                    print("Пропускаем")
                value = input("Добавим оливки(Y/N)?: ")
                if value == "y":
                    pizza.add_olives()
                    self.chek.append("\tОливки\n")
                else:
                    print("Пропускаем")
                value = input("Добавим сладкий лук(Y/N)?: ")
                if value == "y":
                    pizza.add_cucumber()
                    self.chek.append("\tСладкий лук\n")
                else:
                    print("Пропускаем")
                value = input("Добавим чили(Y/N)?: ")
                if value == "y":
                    pizza.add_cucumber()
                    self.chek.append("\tчили\n")
                else:
                    print("Пропускаем")
                print("Ваша пицца готова")
            else:
                print("Ваша пицца готова")
            value = input("Добавим еще одну пиццу(Y/N)?: ")
            if value == "n":
                break

        self.chek.append("Общая сумма: ")
        self.chek.append(str(self.full_price))
        value = input("Оплата по карте?-нажмите 1, или наличными? - нажмите 2: ")

        if value == "1":
            self.chek.append("\nОплата по карте")
        if value == "2":
            self.chek.append("\nОплата наличными")

        self.statistika.append("Четыре сыра: ")
        self.statistika.append(str(self.qt_four_cheeses))
        self.statistika.append("\nГавайская: ")
        self.statistika.append(str(self.qt_hawai))
        self.statistika.append("\nПепперони: ")
        self.statistika.append(str(self.qt_pepperoni))
        self.statistika.append("\nКарбонара: ")
        self.statistika.append(str(self.qt_carbonara))
        self.statistika.append("\nВегетарианская: ")
        self.statistika.append(str(self.qt_vegan))
        self.statistika.append("\nОбщая сумма: ")
        self.statistika.append(str(self.full_price))

        print("".join(self.chek))


class Write:
    def write_chek(chek):
        with open("check.txt", "w", encoding="utf-8") as f:
            f.write("".join(chek))

    def write_stat(stat):
        with open("statistika.txt", "w", encoding="utf-8") as f:
            f.write("".join(stat))


if __name__ == '__main__':
    menu = Menu()
    pizza = Standart_pizza()
    menu.menu()
    chek = menu.chek
    stat = menu.statistika
    Write.write_chek(chek)
    Write.write_stat(stat)
