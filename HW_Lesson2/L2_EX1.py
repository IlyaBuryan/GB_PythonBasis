"""
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

my_list = [1, "Строка", (1, 2), 5.5, [3, 4, 5], {"a":1, "b":2}, True]
for i in my_list:
    print(type(i))
