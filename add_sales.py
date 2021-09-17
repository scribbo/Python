def add_sales(p):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(p + '\n')


add_sales(input())
