class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.x = complex(a, b)

    def __add__(self, other):
        return "Сумма комплексных чисел --> " + str(self.x + other.x)

    def __mul__(self, other):
        return f"Произведение комплексных чисел --> {str(self.x * other.x)}"


a = ComplexNumber(10, 2)
b = ComplexNumber(15, 7)

print(a.x, b.x)
print(a + b)
print(a * b)
