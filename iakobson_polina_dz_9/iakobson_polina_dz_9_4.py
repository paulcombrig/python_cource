# Задание 4
#
# Реализуйте базовый класс Car

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'car is moving')

    def stop(self):
        print(f'car has stopped')

    def turn(self, direction='forward'):
        print(f'car moves {direction}')

    def show_speed(self, speed):
        print(f'current speed is {speed} km/h')

class TownCar(Car):
    def show_speed(self, speed):
        if speed > 60:
            print(f'Ваша скорость выше допустимой в 60 км/ч')
        else:
            super().show_speed(speed)
class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self, speed):
        if speed > 40:
            print(f'Ваша скорость выше допустимой в 40 км/ч')
        else: super().show_speed(speed)

class PoliceCar(Car):
    pass

# Отработка методов родительского класса
ordinary_car = Car(80, 'red', 'honda', 'no')
ordinary_car.go()
ordinary_car.stop()
ordinary_car.turn('left')
ordinary_car.show_speed(80)

# Переопределение методов
another_town_car = TownCar(65, 'yellow', 'opel', 'no')
another_town_car.show_speed(65)
another_town_car.turn('right')

another_work_car = WorkCar(8, 'white', 'Man', 'no')
another_work_car.show_speed(8)
another_work_car.turn('aback')