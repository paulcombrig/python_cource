# Задание 5
#
# Реализовать класс Stationery (канцелярская принадлежность)

class Stationery():
    def __int__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        super().draw()
        print('Пишем ручкой')

class Pencil (Stationery):
    def draw(self):
        super().draw()
        print('Пишем карандашом')

class Handle(Stationery):
    def draw(self):
        super().draw()
        print('Вооружаемся маркером')


sta = Stationery()
sta.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()