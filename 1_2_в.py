my_list = []

for i in range(1, 1000):
    if i % 2 != 0:
        my_list.append(i ** 3)

total_sum = 0

for el in my_list:
    sum_el = 0
    n = el + 17
    while n > 0:
        sum_el += (n % 10)
        n //= 10
    if sum_el % 7 == 0:
        total_sum += el +17

print(f' Сумма чисел, сумма цифр которых делится на 7 равна {total_sum}')
