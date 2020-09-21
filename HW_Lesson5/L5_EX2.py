"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке
"""

# Вариант 1 - с двойным чтением
with open("my_file_L5_EX2.txt", "r", encoding='utf-8') as open_file:
    print("Количество строк в файле:", len(open_file.readlines()))
    open_file.seek(0)
    num = 0
    for i in open_file:
        num += 1
        print(f"Количество слов в строке {num} '{i.strip()}' --> {len(i.split())}")

# Вариант 2 - с одинарным чтением
with open("my_file_L5_EX2.txt", "r", encoding='utf-8') as open_file:
    num = 0
    for i in open_file:
        num += 1
        print(f"Количество слов в строке {num} '{i.strip()}' --> {len(i.split())}")
    print("Количество строк в файле:", num)
