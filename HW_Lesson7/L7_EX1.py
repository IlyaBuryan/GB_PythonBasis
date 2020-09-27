from copy import deepcopy


class Matrix:

    def __init__(self, matrixia):
        self.matrixia = matrixia

    def __add__(self, other):
        if len(self.matrixia) == len(other.matrixia) and len(self.matrixia[0]) == len(other.matrixia[0]):
            rows = deepcopy(self.matrixia)
            for i in range(len(self.matrixia)):
                for j in range(len(self.matrixia[i])):
                    rows[i][j] += other.matrixia[i][j]
            return Matrix(rows)
        else:
            return "Вы пытаетесь сложить неравные матрицы.  Операция запрещена!"

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, i)) for i in self.matrixia])


a = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
b = Matrix([[3, 5, 32], [2, 4, 6]])
c = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, 8]])
print(a)
print()
print(b)
print()
print(c)
print()
print(a + b)
print()
print(a + c)
