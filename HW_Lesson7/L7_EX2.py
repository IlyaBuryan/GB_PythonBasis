from abc import ABC, abstractmethod

"""
Задание для меня было очень сложное в плане понимания что надо сделать и какой ожидается результат. 
3 класса реализованы, метод property и настройка параметра использованы,создан сбстрактный класс для Clothes.
Сумма полностью считается. Надеюсь это все, что нужно.
"""


# Вариант 1 - тип и размер одежды вводится при методе "add_cloths"
class Clothes(ABC):
    def __init__(self):
        self.a = []

    def add_cloths(self, type, size):
        self.__type = type
        self.size = size
        if self.__type == "suit":
            self.a.append(Suit(self.size))
        if self.__type == "coat":
            self.a.append(Coat(self.size))

    @abstractmethod
    def full_sum(self):
        pass


class Coat():
    def __init__(self, size):
        self.fabric = size / 6.5 + 0.5


class Suit():
    def __init__(self, size):
        self.fabric = size * 2 + 0.3


class Clothes2(Clothes):
    @property
    def full_sum(self):
        full_sum = 0
        for i in self.a:
            full_sum += i.fabric
        return round(full_sum, 5)


a = Clothes2()
a.add_cloths("suit", 10)
a.add_cloths("coat", 65)
a.add_cloths("unknown", 15)
a.add_cloths("suit", 10)
a.add_cloths("suitn", 10)
a.add_cloths("coat", 10)
a.add_cloths("suit", 5)
print("Сумма затраченного материала:", a.full_sum)

"""
Вариант 2 - у класса есть переменная типа, методе "add_cloths" принимает только размер. Чтобы добавлять новые типы
необходимо изменить переменную type  у экземпляра класса.
Так же добавлена проверка элемента typeБ если он не равен ни coat ни suit, то изменить на coat, чтобы применять формулу
"""

"""
class Clothes(ABC):
    def __init__(self, type):
        self.a = []
        self.type = type

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        if type == 'suit':
            self.__type = "suit"
        elif type == 'coat':
            self.__type = "coat"
        else:
            self.__type = "coat"

    def add_cloths(self, size):
        self.size = size
        if self.__type == "suit":
            self.a.append(Suit(self.size))
        if self.__type == "coat":
            self.a.append(Coat(self.size))

    @abstractmethod
    def full_sum(self):
        pass


class Coat():
    def __init__(self, size):
        self.fabric = size / 6.5 + 0.5


class Suit():
    def __init__(self, size):
        self.fabric = size * 2 + 0.3


class Clothes2(Clothes):
    @property
    def full_sum(self):
        full_sum = 0
        for i in self.a:
            full_sum += i.fabric
        return full_sum


a = Clothes2("sudfit")
a.add_cloths(10)
a.add_cloths(10)
a.type = "suit"
a.add_cloths(10)
a.add_cloths(10)
print("Сумма затраченного материала:", a.full_sum)
"""
