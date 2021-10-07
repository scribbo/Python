class DelError(Exception):
    def __init__(self, txt):
        self.txt = txt


a, b = list(map(int, input('Enter dividend and divisor ').split()))

try:
    if b == 0:
        raise DelError('Cannot be divided by zero!')
except (ZeroDivisionError, DelError) as err:
    print(err)
    print(1)
else:
    print(round(a / b, 2))
