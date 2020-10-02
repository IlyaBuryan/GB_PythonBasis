class Warehouse:
    full_warehouse = {"managers": [], "traders": [], "olddepartment": []}
    count_tech = {"managers": 0,
                  "traders": 0,
                  "olddepartment": 0}

    def to_take(self, subj):
        if subj:
            if subj[1] == "Printer":
                self.full_warehouse["managers"].append(subj)
                self.count_tech["managers"] += 1
            elif subj[1] == "Scaner":
                self.full_warehouse["traders"].append(subj)
                self.count_tech["traders"] += 1
            elif subj[1] == "Xerox":
                self.full_warehouse["olddepartment"].append(subj)
                self.count_tech["olddepartment"] += 1


class Technic:
    def __init__(self):
        self.producer = "HP"


class Prin(Technic):
    name = "Printer"

    def distinct(self, price, speed):
        self.price = price
        try:
            self.speed = speed
            self.speed = int(self.speed)
            return [self.producer, self.name, self.price, self.speed]
        except:
            print(f"Для Printer значение speed !!{self.speed}!! не может быть строковым. Техника не добавлена.")


class Scan(Technic):
    name = "Scaner"

    def distinct(self, price, speed):
        self.price = price
        try:
            self.speed = speed
            self.speed = int(self.speed)
            return [self.producer, self.name, self.price, self.speed]
        except:
            print(f"Для Scaner значение speed !!{self.speed}!! не может быть строковым. Техника не добавлена.")


class Xerox(Technic):
    name = "Xerox"

    def distinct(self, price, speed):
        self.price = price
        try:
            self.speed = speed
            self.speed = int(self.speed)
            return [self.producer, self.name, self.price, self.speed]
        except:
            print(f"Для Xerox значение speed !!{self.speed}!! не может быть строковым. Техника не добавлена.")


war = Warehouse()
war.to_take(Prin().distinct(100, 100))
war.to_take(Scan().distinct(5476, 15))
war.to_take(Xerox().distinct(199, 2))
war.to_take(Prin().distinct(13240, 99))
war.to_take(Prin().distinct(13240, "66 lists"))

print("Список всей техники на складе по департаментам: ", war.full_warehouse)
print("Количество техники на складе по департаментам: ", war.count_tech)
