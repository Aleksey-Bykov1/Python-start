class Cell:
    def __init__(self, nums):
        self.nums = nums

    def __add__(self, other):
        return print(f'Сумма ячеек клеток -> {Cell(self.nums + other.nums)}')

    def __sub__(self, other):
        if self.nums > other.nums:
            return print(f'Разность колличества ячеек клеток -> {Cell(self.nums - other.nums)} ')
        else:
            return print(f'Вычитание не возможно, ячеек в первой клетке меньше')

    def __mul__(self, other):
        return print(f'Умножение ячеек клетки -> {Cell(self.nums * other.nums)}')

    def __floordiv__(self, other):
        return print(f'Деление ячеек клетки -> {Cell(self.nums // other.nums)}')

    def make_oder(self, nucleus):
        return print('\n'.join(['o' * nucleus for i in range(self.nums // nucleus)]) \
                     + '\n' + 'o' * (self.nums % nucleus))

    def __str__(self):
        return str(f'{self.nums}')


n = Cell(12)
m = Cell(9)

n + m
n * m
n - m
n // m
n.make_oder(5)
