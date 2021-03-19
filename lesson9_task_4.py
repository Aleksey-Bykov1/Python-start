from random import choice, randint


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Car go-go!")

    def stop(self):
        print('Car stop.')

    def turn(self):
        print(choice(['left', 'right', 'forward', 'back']))

    def show_speed(self):
        return print(randint(0, 140))


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        car_speed = randint(0, 200)
        print(f'TownCar {car_speed}')
        if car_speed > 60:
            print("TownCar Over speed")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        car_speed = randint(0, 300)
        print(f'SportCar {car_speed}')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        car_speed = randint(0, 120)
        print(f'WorkCar {car_speed}')
        if car_speed > 40:
            print("WorkCar Over speed")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=True)

    def show_speed(self):
        car_speed = randint(0, 250)
        print(f'PoliceCar {car_speed}')


a = TownCar(200, 'red', 'Mazda')
a.show_speed()
a.turn()
print()

a_1 = SportCar(300, 'pink', 'Maserati')
a_1.show_speed()
a_1.turn()
print()

a_2 = WorkCar(120, 'yellow', 'Cat')
a_2.show_speed()
a_2.turn()
print()

a_3 = PoliceCar(200, 'red', 'Mazda')
a_3.show_speed()
a_3.turn()
