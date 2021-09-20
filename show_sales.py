import time

def show_sales(*args):

    with open('bakery.csv', 'r', encoding='utf-8') as f:
        if len(args) == 0:
            print(f.read())

        elif len(args) == 1:
            str_1 = f.read()
            print(*str_1.split('\n')[int(args[0]) - 1:], sep='\n')

        else:
            str_2 = f.read()
            print(*str_2.split('\n')[int(args[0]) - 1: int(args[1])], sep='\n')


x = input().split(' ')
start_time = time.time()
show_sales(*x)
print(time.time() - start_time)

