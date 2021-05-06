# Задание 1
# Создать класс TrafficLight (светофор).

from itertools import cycle

class TrafficLight():
    def __init__(self, __color, timeout):
        self.__color = 'red'
        self.timeout = timeout

    def running(self):
        cycler = cycle(['red', 'yellow', 'green'])
        for tr_color in cycler:
            self.__color = tr_color
            if tr_color == 'red':
                self.timeout = 7
            elif tr_color == 'yellow':
                self.timeout = 2
            else:
                self.timeout = 8
            print (f'{tr_color} color has timeout in {self.timeout} seconds')

tr_light = TrafficLight('red', 0)
tr_light.running()


