class Road:
    def __init__(self, length, thickness, width):
        self._length = length
        self._width = width
        self._thickness = thickness
        self._weight = 0.025

    def payment(self):
        return print(self._length * self._width * self._thickness * self._weight)

a = Road(20, 5000, 5)
a.payment()
