from itertools import islice
import time

def show_sales_2(*args):

    with open('bakery.csv', 'r', encoding='utf-8') as f:
        if len(args) == 0:
            print(f.read())

        elif len(args) == 1:
            for line in islice(f, int(args[0]) - 1, None):
                print(line, end='')

        else:
            for line in islice(f, int(args[0]) - 1, int(args[1])):
                print(line, end='')


x = input().split(' ')
start_time = time.time()
show_sales_2(*x)
print(time.time() - start_time)
