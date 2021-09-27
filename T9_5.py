class Stationery:
    def __init__(self, title):
        self.t = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Толщина линии равна 0.5 мм')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш остро заточен')


class Handle(Stationery):
    def draw(self):
        print('Маркер засох')


item_1 = Pen('parker')
item_1.draw()

item_2 = Pencil('bic')
item_2.draw()

item_3 = Handle('attache')
item_3.draw()