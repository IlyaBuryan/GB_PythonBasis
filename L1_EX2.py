# Можно было бы добавить отбрасывание целоых суток, чтобы число часов было максимум 24, по у условии этого
# не просилось, поэтому не добавил :)

time = int(input("Введите, пожалуйста, время в секундах: "))

hours = time // 3600
if hours < 10:
    hours = "0" + str(hours)

minutes = (time % 3600) // 60
if minutes < 10:
    minutes = "0" + str(minutes)

seconds = (time % 3600) % 60
if seconds < 10:
    seconds = "0" + str(seconds)

print(f"{time} секунд = {hours}:{minutes}:{seconds}")
