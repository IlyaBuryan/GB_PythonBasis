"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
"""

# Проверка на наличие ошибок, если будет обнаружена проблема с форматом, то файл не будет создан
import os

with open("text_4.txt", "r", encoding='utf-8') as open_file:
    ru_dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    with open("my_file_L5_EX4.txt", "w", encoding='utf-8') as new_file:
        try:
            list_raw = open_file.readline().split()
            while list_raw:
                list_raw[0] = ru_dic[list_raw[0]]
                print(' '.join(list_raw), file=new_file)
                list_raw = open_file.readline().split()
            print("Новый файл записан без ошибок!")
        except:
            print("Ошибка записи, проверьте формат исходного файла!")
            new_file.close()
            os.remove("my_file_L5_EX4.txt")
