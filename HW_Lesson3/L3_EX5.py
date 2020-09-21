"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных
пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ
введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме
и после этого завершить программу.
"""

# Вариант 1 - Короткий без функций
t = True
full_sum = 0
while t:
    try:
        sequence = list(input("Введите последовательность чисел, разделенных пробелом "
                              "(для прекращения счета введите ':' двоеточие): ").split())
        if ":" in sequence:
            sequence = sequence[:sequence.index(":")]
            t = False
        full_sum += sum(map(float, sequence))
        print("Полная сумма: ", full_sum)
    except ValueError:
        print("Неверный ввод. Введите последовательность чисел или спец. символ ':'!")
        print("Полная сумма: ", full_sum)


# Вариант 2 - длинный с функциями, глобал переменной и без стандартной sum().
# Написал на случай, если первый вариант решения не подойдет к теме и в целом для тренеровки и практики.
t = True


def sum_list(sequence_f):
    """Вычисление суммы списка до спец символа :

    Функция перебирает последовательность приводя каждую переменную к формату float, пока не встретит : (остальные
    элементы последовательности после : игнорируются). Так же меняется значение глобальной переменной t на False, 
    чтобы окончить цикл вызывающей функции
    Значение каждого элемента прибавляется к общей сумме, которая возвращается в качестве результата функции. 
    Если элемент последовательности не будет являться числом, то функция выдаст ошибку ввода, а сумму не вернет.

    """
    global t
    i = 0
    full_sum2 = 0
    while i < len(sequence_f):
        if sequence_f[i] == ':':
            t = False
            break
        else:
            try:
                full_sum2 += float(sequence_f[i])
            except ValueError:
                print("Неверный ввод. Введите числа или спец. символ ':'!")
                full_sum2 = 0
                break
        i += 1
    return full_sum2


def ask():
    """Функция для запроса последовательностей и вычисления общей суммы

    Функция запрашивает последовательности. Затем передает последовательности в функцию sum_list чтобы она
    вычислила и вернула сумму и сообщила, если найдет : в последовательности (путем изменения глобальной 
    переменной t на False)

    """
    full_sum2 = 0
    while t:
        sequence_f = list(input("Введите последовательность чисел, "
                                "разделенных пробелом (для прекращения счета введите ':') : ").split())
        full_sum2 += sum_list(sequence_f)
        print("Полная сумма: ", full_sum2)


ask()
