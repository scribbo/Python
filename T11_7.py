class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return Complex(self.re * other.re - self.im * other.im, self.re * other.im + other.re * self.im)

    def __str__(self):
        if self.im > 0:
            return str(self.re) + '+' + str(self.im) + 'i'
        elif self.im < 0:
            return str(self.re) + str(self.im) + 'i'
        else:
            return str(self.re)


z = Complex(5, 0)
z1 = Complex(5, 4)
z2 = Complex(5, -3)
print(z)
print(z1)
print(z2)
print(z1 + z2)
print(z1 * z2)
