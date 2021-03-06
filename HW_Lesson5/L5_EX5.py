"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран
"""

with open("my_file_L5_EX5.txt", "w+", encoding='utf-8') as file:
    print(input("Введите набор чисел, разделенных пробелами: "), file=file)
    file.seek(0)
    try:
        file_output = file.read().split()
        print(f"{sum(map(float, file_output))} --> сумма записанных в файле чисел: {' '.join(file_output)}")
    except ValueError:
        print("В файле записаны не числа. Пожалуйста, заполните файл числами, разделенными пробелами!")
