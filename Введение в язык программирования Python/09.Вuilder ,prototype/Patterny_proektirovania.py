############ 1 ################ Вuilder(строитель)

class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getCar(self):
        car = Car()     # внутри класса объект другого класса

        # корпус
        body = self.__builder.getBody()
        car.setBody(body) # вызов метода класса Car

        # двигатель
        engine = self.__builder.getEngine()
        car.setEngine(engine)

        # колеса 4
        i = 0
        while i < 4:
            wheel = self.__builder.getWheel()
            car.attachWheel(wheel)
            i += 1

        return car

class Car:
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    #установка корпуса
    def setBody(self,body):
        self.__body = body
    # Установка колеса(1)
    def attachWheel(self, wheel):
        self.__wheels.append(wheel)
    # устанока двигателя
    def setEngine(self,engine):
        self.__engine = engine

    def specification(self):
        print(f"Body: {self.__body.shape}")
        print(f"Engine horsepower: {self.__engine.horsepower}")
        print(f"Tire_size: {self.__wheels[0].size}")
#*********
class Builder:
    def getWheel(self):
        pass
    def getEngine(self):
        pass
    def getBody(self):
        pass
#*****************
class JeepBuilder(Builder):
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22
        return  wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def getBody(self):
        body = Body()
        body.shape = "SUV"
        return body

#**********детали**********
class Wheel:
    wheel = None
class Engine:
    horsepower = None
class Body:
    body = None

#******** MAIN ***********
print("Марка: Jeep")
jeepBuilder = JeepBuilder()
director = Director()
#сборка Джипа
director.setBuilder(jeepBuilder)
jeep = director.getCar()
jeep.specification()
print("")

######### 3 ################# Prototype

import copy


class Prototype:
    _type = None
    _value = None

    def clone(self):
        pass

    def getType(self):
        return self._type

    def getValue(self):
        return self._value

#*************************
class Type1(Prototype):

    def __init__(self, number):
        self._type = "Type1"
        self._value = number

    def clone(self):
        return copy.copy(self)

#***************************
class Type2(Prototype):

    def __init__(self, number):
        self._type = "Type2"
        self._value = number

    def clone(self):
        return copy.copy(self)

#******************************
class ObjectFactory:
    __type1Value1 = None
    __type1Value2 = None
    __type2Value1 = None
    __type2Value2 = None

    @staticmethod
    def initialize():
        ObjectFactory.__type1Value1 = Type1(1)
        ObjectFactory.__type1Value2 = Type1(2)
        ObjectFactory.__type2Value1 = Type1(1)
        ObjectFactory.__type2Value2 = Type1(2)

    @staticmethod
    def getType1Value1():
        return  ObjectFactory.__type1Value1.clone()
    @staticmethod
    def getType1Value2():
        return  ObjectFactory.__type1Value2.clone()
    @staticmethod
    def getType2Value1():
        return  ObjectFactory.__type2Value1.clone()
    @staticmethod
    def getType2Value2():
        return  ObjectFactory.__type2Value2.clone()


#***********MAIN***************
ObjectFactory.initialize()

# instance = ObjectFactory.getType1Value1()
# print(f"{instance.getType()}: {instance.getValue()}")
#
# instance = ObjectFactory.getType1Value2()
# print(f"{instance.getType()}: {instance.getValue()}")
#
# instance = ObjectFactory.getType2Value1()
# print(f"{instance.getType()}: {instance.getValue()}")
#
# instance = ObjectFactory.getType2Value2()
# print(f"{instance.getType()}: {instance.getValue()}")


############### 3 ################# Паста

class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getPasta(self):
        pasta = Pasta()

        type = self.__builder.getType()
        pasta.setType(type)

        sauce = self.__builder.getSauce()
        pasta.setSauce(sauce)

        filling = self.__builder.getFilling()
        pasta.setFilling(filling)

        additive = self.__builder.getAdditive()
        pasta.setAdditive(additive)

        return pasta


class Pasta:
    def __init__(self):
        self.__type = None
        self.__sauce = None
        self.__filling = None
        self.__additive = None

    def setType(self, type):
        self.__type = type

    def setSauce(self, sauce):
        self.__sauce = sauce

    def setFilling(self, filling):
        self.__filling = filling

    def setAdditive(self, additive):
        self.__additive = additive

    def specification(self):
        print(f"\tТип макарон: {self.__type}\n\tСоус: {self.__sauce}\n\tНачинка: {self.__filling}\n\tДобавки: {self.__additive}")


class Builder:
    def getType(self):  # тип
        pass

    def getSauce(self):  # соус
        pass

    def getFilling(self):  # начинка
        pass

    def getAdditive(self):  # добавка
        pass


class CarbonaraBuilder(Builder):
    def getType(self):
        type = "Спагетти"
        return type
    def getSauce(self):
        sause = "Карбонара"
        return sause
    def getFilling(self):
        filling = "Бекон"
        return filling
    def getAdditive(self):
        additive = "Перец, сыр"
        return additive

class BoloneseBuilder(Builder):
    def getType(self):
        type = "Спагетти"
        return  type
    def getSauce(self):
        sause = "Болоньезе"
        return sause
    def getFilling(self):
        filling = "Фарш"
        return filling
    def getAdditive(self):
        additive = "Зелень"
        return additive

class FlotBuilder(Builder):
    def getType(self):
        type = "Рожки"
        return  type
    def getSauce(self):
        sause = "Кетчинез"
        return sause
    def getFilling(self):
        filling = "Фарш"
        return filling
    def getAdditive(self):
        additive = "Перец"
        return additive


if __name__ == '__main__':

    print("Карбонара")
    carbonaraBuilder = CarbonaraBuilder()
    director = Director()
    director.setBuilder(carbonaraBuilder)
    carbonara = director.getPasta()
    carbonara.specification()

    print("По-флотски")
    flotBuilder = FlotBuilder()
    director = Director()
    director.setBuilder(flotBuilder)
    flot = director.getPasta()
    flot.specification()

    print("Болоньезе")
    boloneseBuilder = BoloneseBuilder()
    director = Director()
    director.setBuilder(boloneseBuilder)
    bolonese = director.getPasta()
    bolonese.specification()


