
first_result = float(input("Введите количество километров, которое спортсмен пробежал в первый день: "))
goal_result = float(input("Введите количество километров, которое спортсмен должен пробегать: "))

days = 1
while first_result < goal_result:
    first_result = round(first_result + first_result * 0.1, 2)
    days += 1

print(f"На {days}-й день спортсмен достигнет результата — не менее {goal_result} км.")
