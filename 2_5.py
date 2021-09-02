prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
str = []
str_sort = []

for el in prices:
    str.append(f'{int(el):02d} руб. {int((el % 1) * 100):02d} коп.')

print(', '.join(str))
print(f' ID списка {id(prices)}')

prices.sort()

print(prices)
print(f' ID отсортированного списка {id(prices)}')

prices_sort = sorted(prices, reverse=True)
print(prices_sort)
print(f'Цены 5-ти самых дорогих товаров: {prices_sort[:5]}')


