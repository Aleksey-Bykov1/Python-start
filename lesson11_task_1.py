class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def m_1(cls, data):
        try:
            d, m, y = map(int, data.split('.'))
            return d, m, y
        except ValueError:
            print("Вводите только числа")

    @staticmethod
    def m_2(data):
        try:
            if 0 >= data[0] or data[0] > 31:
                print("Введите корректный день месяца от 1 до 31")
            elif 0 >= data[1] or data[1] > 12:
                print('Введите корректный месяц от 1 до 12 ')
            elif 0 >= data[2] or data[2] > 9999:
                print("Введите корректный год от 1 до 9999")
        except ValueError:
            print("Вводите только числа")
        else:
            print("Вы ввели корректные данные все прошло успешно")
            return print(*data)


one = Data.m_1('28.03.2021')

print(Data.m_2(one))
