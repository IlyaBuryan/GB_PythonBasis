"""
Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников
"""

with open("text_3.txt", "r", encoding='utf-8') as open_file:
    try:
        full_list = open_file.readlines()
        length = len(full_list)
        average = 0
        for i in range(length):
            salary = round(float(full_list[i].split()[-1]), 2)
            if salary < 20000:
                print(full_list[i].split()[0], salary)
            average += salary
        print("Средняя зарплата: ", round(average / length, 2))
    except:
        print("Ошибка чтения, проверьте файл!")
