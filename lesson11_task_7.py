class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, obj):
        self.addx = self.x + obj.x
        self.addy = self.y + obj.y

    def __mul__(self, obj):
        self.mulx = self.x * obj.x - self.y * obj.y
        self.muly = self.y * obj.x + self.x * obj.y


a = Complex(1, 2)
b = Complex(3, 4)
a + b
a * b
print(f'Результат сложения: {a.addx:.2f} + {a.addy:.2f}i')
print(f'Результат умножения: {a.mulx:.2f} + {a.muly:.2f}i')

