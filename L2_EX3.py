"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

# List
year_list = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
try:
    month_list = int(input("Введите номер месяца от 1 до 12: "))
    print(f"Время года {month_list}-го месяца: {year_list[month_list - 1]}")
except:
    print("Вы ввели неверный номер месяца. Попробуйте снова")

# Dict
year_dic = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень",
            10: "Осень", 11: "Осень", 12: "Зима"}
try:
    month_dic = int(input("Введите номер месяца от 1 до 12: "))
    print(f"Время года {month_dic}-го месяца: {year_dic[month_dic]}")
except:
    print("Вы ввели неверный номер месяца. Попробуйте снова")
