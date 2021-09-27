class Road:
    def __init__(self, length, width):
        self._l = length
        self._w = width

    def my_weight(self):
        sum_w = self._l * self._w * (25/1000) * (5/100)
        print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна длиной {self._l} метров и шириной {self._w} метров составляет {sum_w} тонн.')


road1 = Road(100, 500)
road1.my_weight()
