class NotNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


a = []
while True:
    next_el = input("Введите значение или завершите командой 'stop': ")
    if next_el == 'stop':
        if len(a) == 0:
            print("В списке ничего нет!")
        else:
            print("Список состоящий только из чисел", a)
        break
    else:
        try:
            if next_el.lstrip("-").isdigit():
                a.append(float(next_el))
            else:
                raise NotNumber("Введено не число. Будьте внимательны!")
        except NotNumber as err:
            print(err)
