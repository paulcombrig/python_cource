# Задание 2
# Реализовать класс Road (дорога)

class Road():
    def __init__(self, length=20, width=50000):
        self._length = length
        self._width = width

    def mass_calculate(self):
        thickness_sm = 5
        mass_sm = 25
        area = self._length * self._width * thickness_sm * mass_sm
        return area

road_mass = Road()
mass = road_mass.mass_calculate()
print(f'Масса асфальта для укладки дороги площадью {road_mass._length * road_mass._width} '
      f'равна {mass} кг')