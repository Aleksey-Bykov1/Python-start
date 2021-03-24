class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str('\n'.join(['\t '.join([str(i) for i in j]) for j in self.data]))

    def __add__(self, other):
        try:
            m = Matrix([[int(a) + int(b) for a, b in zip(my_row, other_row)]
                        for my_row, other_row in zip(self.data, other.data)])
            return m
        except ValueError as err:
            print(f' {err} В матрице должны быть только числа')  # исключение если в матрице есть не цифра


x = Matrix([['1', '3', 3.3, 4], [2, '3', 4, 6], [2, 4, 6]])
y = Matrix([[10, 10, '1', 10], [10, 10, 10, 10], [2, 5]])

print(x)
print()
print(y)
print()
print(x + y)
