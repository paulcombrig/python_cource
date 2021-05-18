# Задание 2

# Реализовать проект расчета суммарного расхода ткани на производство
# одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь
# определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих
# методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные
# на этом уроке знания: реализовать абстрактные классы для основных классов
# проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Bekleidung(ABC):

    def __init__(self, option):
        self.option = option

    @abstractmethod
    def find_matherial(self):
        pass

class Mantel(Bekleidung):

    @property
    def find_matherial(self):
        return round((self.option / 6.5) + 0.5)

class Hosen(Bekleidung):

    @property
    def find_matherial(self):
        return round(2 * self.option + 0.3)


mantel = Mantel(68)
hose = Hosen(73)
print(mantel.find_matherial)
print(hose.find_matherial)