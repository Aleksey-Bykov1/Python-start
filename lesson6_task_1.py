"""
    В программе создается отдельный файл logs_result.txt, для удобства проверки полученных данных.
    Так же программа запрашивает колличество элементов для вывода в терминал, для оптимизации.
    При выводе показывается номер элемента, что соответствует номеру строки в исходном файле.
    Итоговый список line_3 создается согласно условиям к задаче №1 и записывается в logs.txt.
"""

with open('nginx_logs.txt', 'r', encoding='utf-8') as logs:
    line_3 = []
    for line in logs:
        line_1 = line.replace('-', '').replace('"', '').split()
        line_2 = line_1[0], line_1[3], line_1[4]
        with open('logs_result.txt', 'a', encoding='utf-8') as res:  # Создаю отдельный отсортированный файл лог
            res.write(f'{line_2}\n')
        line_3.append(line_2)  # Итоговый список с необходимой информацией
n = int(input('Введите колличество элементов для вывода -> '))
for i in range(n):
    print(i + 1, line_3[i])

with open('logs.txt', 'w', encoding='utf-8') as f:
    f.writelines(str(line_3))
