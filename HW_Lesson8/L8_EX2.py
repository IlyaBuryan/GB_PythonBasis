class ZeroDivError(Exception):
    def __init__(self, txt):
        self.txt = txt


up = float(input("Введите числитель: "))
down = float(input("Введите знаменатель: "))

try:
    if down == 0:
        raise ZeroDivError("Деление на 0 запрещено!")
except ZeroDivError as err:
    print(err)
else:
    print(f"Результат деления: {round(up / down, 2)}")
