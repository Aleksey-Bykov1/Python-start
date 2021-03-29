class Store:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.product_dict = {'Наименование': self.name, 'Цена': self.price, 'Колличество': self.quantity}

    def moving(self):
        try:
            product_n = input(f'Введите наименование ')
            product_p = int(input(f'Введите цену за ед '))
            product_q = int(input(f'Введите количество '))
            product = {'Наименование': product_n, 'Цена': product_p, 'Колличество': product_q}
            self.product_dict.update(product)
        except:
            return f'Ошибка ввода'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            print(f'Весь склад -\n {self.product_dict}')
            return f'Выход'
        else:
            return Store.moving(self)


class OfficeEquipment(Store):
    def __init__(self, name, price, quantity, kind):
        super().__init__(name, price, quantity)
        self.type = kind


class Printer(OfficeEquipment):
    def __init__(self, name, price, quantity, kind, time_work):
        super().__init__(name, price, quantity, kind)
        self.time_work = time_work

    def work_printer(self):
        return f'Печатаю разный текст уже {self.time_work} минут'


class Scanner(OfficeEquipment):
    def __init__(self, name, price, quantity, kind, time_work):
        super().__init__(name, price, quantity, kind)
        self.time_work = time_work

    def work_scanner(self):
        return f'Сканирую разный текст уже {self.time_work} минут'


class Xerox(OfficeEquipment):
    def __init__(self, name, price, quantity, kind, time_work):
        super().__init__(name, price, quantity, kind)
        self.time_work = time_work

    def work_xerox(self):
        return f'Копирую разный текст уже {self.time_work} минут'


pr = Printer('Canon', 12345, 2, 'printer', 45)
sc = Scanner('Brother', 2345, 6, 'scanner', 21)
xe = Xerox('Xerox', 45678, 8, 'MFU', 12)


print(pr.work_printer())
print(sc.work_scanner())
print(xe.work_xerox())

print(pr.moving())
print(sc.moving())
print(xe.moving())
