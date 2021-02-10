seconds = int(input('Введите колличество секунд -> '))
minutes = 0
hour = 0
day = 0

while seconds >= 60:
    seconds -= 60
    minutes += 1
    if minutes >= 60:
        minutes = 0
        hour += 1
    if hour >= 24:
        hour = 0
        day += 1

print(day, "дн", hour, "час", minutes, "мин", seconds, "сек")
