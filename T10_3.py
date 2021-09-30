class Cell:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return f' n = {self.n}'

    def __add__(self, other):
        return Cell(self.n + other.n)

    def __sub__(self, other):
        if self.n > other.n:
            return Cell(self.n - other.n)
        else:
            return 'Разность количества ячеек двух клеток должна быть больше нуля'

    def __mul__(self, other):
        return Cell(self.n * other.n)

    def __truediv__(self, other):
        if other.n != 0:
            return Cell(self.n // other.n)
        else:
            return 'Количество ячеек клетки - делителя должна быть больше нуля'

    def make_order(self, number):
        if number > 0:
            k = self.n // number
            ost = self.n % number
            my_str = '*' * number
            last_str = '*' * ost
            for i in range(k):
                print(my_str)
            print(last_str)


one = Cell(17)
two = Cell(4)
print(one + two)
print(one - two)
print(one * two)
print(one / two)
one.make_order(5)