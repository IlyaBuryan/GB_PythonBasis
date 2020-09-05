benefit = int(input("Введите значение выручки в рублях: "))
loses = int(input("Введите значение издержек в рублях: "))

if benefit > loses:
    print("Фирма работает с прибылью!")
    print(f"Рентабельность выручки: {round(((benefit - loses) / benefit) * 100, 2)}%")
    employee = int(input("Введите количество сотрудников фирмы: "))
    print(f"Прибыль фирмы в расчете на 1 сотрудника составляет {round((benefit - loses) / employee, 2)} рублей")
elif benefit < loses:
    print("Фирма работает в убыток!")
elif benefit == loses:
    print("Фирма работает в ноль, без прибыли или убытка!")
