class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Инструмент для рисования - ручка.')


class Pencil(Stationery):
    def draw(self):
        print('Инструмент для рисования - карандаш.')


class Handle(Stationery):
    def draw(self):
        print('Инструмент для рисования - маркер.')


test = Stationery('Test')
my_pen = Pen('Ручка')
my_pencil = Pencil('Карандаш')
my_handle = Handle('Маркер')

test.draw()
my_pen.draw()
my_pencil.draw()
my_handle.draw()
