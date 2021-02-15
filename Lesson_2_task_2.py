my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
output_list = []
result_list =[]

# добавляю кавычки и добавляю нуль если меньше двух цифр
for ind, val in enumerate(my_list):
    if val.isalpha():
        output_list.append(val)
    elif val.isdigit():
        output_list.extend(['"', val.zfill(2), '"'])
    elif ('+' or '-') in val:  # сделал для значений как с + так и с - . Это же вроде температура.
        output_list.extend(['"', val.zfill(3), '"'])

# убираю пробелы между кавычками и цифрами, вроде в результате строка без пробелов?..
for ind, val in enumerate(output_list):
    if val.isalpha():
        result_list.append(val)
    elif val.isdigit():
        result_list.extend(['"' + val.zfill(2) + '"'])
    elif ('+' or '-') in val:  # сделал для значений как с + так и с - . Это же вроде температура.
        result_list.extend(['"' + val.zfill(3) + '"'])

my_str = ' '.join(result_list)

# вывожу список как в метадичке и строку как в методичке
print(output_list)
print(my_str)


