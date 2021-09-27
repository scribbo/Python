class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.s = speed
        self.c = color
        self.n = name
        self.p = bool(is_police)

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        self.d = direction
        print(f'Машина повернула на{self.d}')

    def show_speed(self):
        print(f'Скорость автомобиля равна {self.s} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.s > 60:
            print('Вы превысили скорость')
        print(f'Скорость автомобиля равна {self.s} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.s > 40:
            print('Вы превысили скорость')
        print(f'Скорость автомобиля равна {self.s} км/ч')


class PoliceCar(Car):
    pass


mazda = TownCar(65, 'red', 'ZZ')
mazda.go()
mazda.stop()
mazda.turn('право')
mazda.show_speed()
print(mazda.p)

volga = WorkCar(35, 'blue', '07')
volga.go()
volga.stop()
volga.turn('лево')
volga.show_speed()
print(volga.c)
print(volga.p)

ferrari = SportCar(120, 'yellow', 'F1')
ferrari.go()
ferrari.stop()
ferrari.turn('право')
ferrari.show_speed()
print(ferrari.c)
print(ferrari.s)
print(ferrari.p)

ford = PoliceCar(60, 'green', 'focus', True)
ford.go()
ford.stop()
ford.turn('право')
ford.show_speed()
print(ford.c)
print(ford.s)
print(ford.p)
