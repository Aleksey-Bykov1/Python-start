numbers_list = []
sum_numbers_list = 0
sum_numbers_list_17 = 0

# наполняю список кубами чисел от 1 до 1000
for i in range(1, 1001, 2):
    numbers_list.append(i ** 3)

# вычисляю сумму тех элементов списка чья сумма цифр делится нацело на 7
for i in numbers_list:
    number = i
    sum_numbers = 0
    flag = False
    while i != 0:
        last_numbers = i % 10
        sum_numbers += last_numbers
        i //= 10
    if sum_numbers % 7 == 0:
        flag = True
    if flag == True:
        sum_numbers_list += number

# добавляю 17 к каждому элементу не перезаписывая список и
# вычисляю сумму тех элементов списка чья сумма цифр делится нацело на 7
for i in numbers_list:
    i += 17
    number = i
    sum_numbers = 0
    flag = False
    while i != 0:
        last_numbers = i % 10
        sum_numbers += last_numbers
        i //= 10
    if sum_numbers % 7 == 0:
        flag = True
    if flag == True:
        sum_numbers_list_17 += number

# вывожу сам список для проверки и результы сумм
print(numbers_list)
print("Сумма элементов списка чьи цифры в сумме кратны 7:", sum_numbers_list)
print("Сумма, увеличенных на 17, элементов списка чьи цифры в сумме кратны 7:", sum_numbers_list_17)
