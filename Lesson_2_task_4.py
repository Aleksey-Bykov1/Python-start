info_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']
my_str = ''

# вывожу приветствие имен с в соответствующем виде без создания нового списка
for i in range(len(info_list)):
    my_str = ''.join(info_list[i])
    name = my_str.split()
    for j in name:
        print(" 'Привет", name[-1].lower().capitalize() + "'")
        break
