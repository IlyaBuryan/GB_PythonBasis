"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

# В методичке написано, что переменные надо переопределять в наследниках, но все работает и так (но переопределил)
class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала!")

    def stop(self):
        print("Машина остановилась!")

    def turn(self):
        print("Машина повернула направо!")

    def show_speed(self):
        print("Текущая сорость", self.speed, "км/ч")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print("Вы превысили скорость! На", self.speed - 60, "км/ч")
        else:
            print("Вы едите с допустимой скоростью!")


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print("Вы превысили скорость! На", self.speed - 40, "км/ч")
        else:
            print("Вы едите с допустимой скоростью!", self.speed, "км/ч")


class PoliceCar(Car):
    pass


class SportCar(Car):
    pass


a = Car(100, "red", "mustang", False)
a.go()
print(a.color, a.name, a.is_police)
a.show_speed()
print()

b = TownCar(45, "blue", "nissan", False)
b.turn()
print(b.color, b.name, b.is_police)
b.show_speed()
print()

c = WorkCar(45, "black", "fiat", False)
c.turn()
print(c.color, c.name, c.is_police)
c.show_speed()
print()

d = PoliceCar(261, "grey", "niva", True)
d.turn()
print(d.color, d.name, d.is_police)
d.show_speed()
print()

e = SportCar(5, "yellow", "ford", False)
e.stop()
print(e.color, e.name, e.is_police)
e.show_speed()
print()
