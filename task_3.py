procent = int(input('Введите колличество процентов от 1 до 20: '))

# вывод ответа для пользователя
if procent == 1:
    print(procent, "процент\n")
elif 1 < procent < 5:
    print(procent, "процента\n")
elif 5 <= procent <= 20:
    print(procent, "процентов\n")
else:
    print("Ну мы так не договаривались.")

# вывод всех склонений для проверки
print("Вывод для проверки")
for i in range(0, 20 + 1):
    if i == 1:
        print(i, "процент")
    elif 1 < i < 5:
        print(i, "процента")
    elif 5 <= i <= 20:
        print(i, "процентов")
