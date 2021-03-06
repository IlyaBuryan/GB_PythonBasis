# Надеюсь понял усложнение задания правильно. каждая функция работает в обоих вариантах

from itertools import count, cycle, chain


# Вариант 1 - с функцией count + break
def my_generator_a(x1=3, x2=10):
    """Итерируемый объект - возвращает целые числа в диапазоне от и до указанных в функции"""
    for i in count(x1):
        if i == x2 + 1:
            break
        else:
            yield i


print("Задача a, вариант 1: ", [i for i in my_generator_a(2, 31)])


# Вариант 2 - через iter и next, без break
def my_generator_a(x1=3, x2=10):
    """Итерируемый объект - возвращает целые числа в диапазоне от и до указанных в функции"""
    a = iter((i for i in range(x1, x2 + 1)))
    for i in range(x2 - x1 + 1):
        yield next(a)


print("Задача a, вариант 2: ", list(my_generator_a(2, 31)))


# Вариант 1 - с функцией cycle + break
def my_generator_b(x1, x2=3):
    """Итерируемый объект - дублирует список заданный в функции число раз или 3 раза, если таковое не задано"""
    f = 0
    for i in cycle([x1]):
        if f == x2:
            break
        else:
            yield i
            f += 1


print("Задача b, вариант 1: ", list(chain.from_iterable([i for i in my_generator_b([23, 1, 3, 10, 4, 11, "a"], 5)])))

my_list = [23, 1, 3, 10, 4, 11, "a"]


# Вариант 2 - через iter и next, без break
def my_generator_b(x1, x2=3):
    """Итерируемый объект - дублирует список заданный в функции число раз или 3 раза, если таковое не задано"""
    for i in range(x2):
        a = iter(x1)
        for j in range(len(x1)):
            yield next(a)


print("Задача b, вариант 2: ", list(my_generator_b(my_list, 5)))

