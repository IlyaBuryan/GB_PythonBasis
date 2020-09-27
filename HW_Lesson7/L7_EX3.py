from random import randint


class Cell:
    def __init__(self):
        self.volume = randint(10, 100)

    def __add__(self, other):
        return "Сумма клеток --> " + str(self.volume + other.volume)

    def __sub__(self, other):
        diff = abs(self.volume - other.volume)
        if diff != 0:
            return "Разница клеток --> " + str(diff)
        else:
            return f"Клетки 1я - ({self.volume}) 2я - ({other.volume}) по замеру одинаковые"

    def __mul__(self, other):
        return "Произведение клеток --> " + str(self.volume * other.volume)

    def __truediv__(self, other):
        if self.volume > other.volume:
            new_cell = int(self.volume / other.volume)
        else:
            new_cell = int(other.volume / self.volume)
        return "Деление клеток --> " + str(new_cell)

    def make_order(self, number):
        self.number = number
        self.example = self.volume
        return str(('*' * self.number + '\n') * (self.example // self.number) + ('*' * (self.example % self.number)))


a = Cell()
print("1-я клетка:", a.volume)

b = Cell()
print("2-я клетка:", b.volume)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a.make_order(10))
