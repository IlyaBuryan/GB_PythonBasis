"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое
слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func()
"""


def int_func(a):
    """Привеодит слово к заглавному типу"""
    return a.title()


def test(a):
    """Проверяет слово на наличие символов кроме маленькой латиницы. Если других символов нет, то вернет True"""
    i = 0
    while i < len(a) and ord(a[i]) in range(97, 123):
        i += 1
    if i == len(a):
        return True


n = input("Введите строку из слов, разделенных пробелом: ").split()
for i in n:
    if test(i):
        print(int_func(i), end=' ')
