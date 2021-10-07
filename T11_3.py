class NumError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []

while True:
    a = input('Enter numbers, for exit - stop ').split()
    stop_det = 0
    for el in a:
        if el.title() == 'Stop':
            stop_det = 1

        else:
            try:
                for j in range(len(el)):
                    if ord(el[j]) < 48 or ord(el[j]) > 57:
                        raise NumError('You only need to enter numbers')

            except NumError as err:
                print(err)
                break
            my_list.append(el)
    if stop_det == 1:
        break

print(my_list)
