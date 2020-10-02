class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def change_date(cls, time):
        return f"Извлеченные из даты чисел --> {int(''.join(time.split('-')))}"

    @staticmethod
    def validate(time):
        a = time.split("-")
        if len(a[0]) != 2 or int(a[0]) > 31 or int(a[0]) < 1:
            return f"Формат дня неверен {a[0]}"
        elif len(a[1]) != 2 or int(a[1]) > 12 or int(a[1]) < 1:
            return f"Формат месяца неверен {a[1]}"
        elif len(a[2]) != 4:
            return f"Формат года неверен! {a[2]}"
        else:
            return f"Дата корректна: {time}"


a = Data("02-09-2019")
print("Дата вызванная через экземпляр -->", a.data)
print(Data.change_date(a.data))
print(Data.validate(a.data))
