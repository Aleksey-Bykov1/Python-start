from abc import ABC, abstractmethod


class Clothes(ABC):
    @property
    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def tissue_consumption(self):
        a = self.size / 6.5 + 0.5
        return print(f'Coat - {a:.2f}')

    @property
    def total(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, growth):
        self.growth = growth

    @property
    def tissue_consumption(self):
        b = (self.growth * 2 + 0.3) / 100
        return print(f'Costume - {b:.2f}')

    @property
    def total(self):
        return (self.growth * 2 + 0.3) / 100

a = Coat(48)
a.tissue_consumption

b = Costume(186)
b.tissue_consumption

print(f'Tissue_consumption - {a.total + b.total:.2f}')
