import time


class TrafficLight:
    __color_1 = 'red'

    def running(self):
        wait = 2
        while wait > 0:
            print('red')
            time.sleep(7)
            print('yellow')
            time.sleep(3)
            print('green')
            time.sleep(7)
            print('yellow')
            time.sleep(3)
            wait -= 1


a = TrafficLight()
a.running()
