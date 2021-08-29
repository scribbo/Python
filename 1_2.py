my_list = []
list_17 = []

for i in range(1, 1000):
    if i % 2 != 0:
        my_list.append(i ** 3)
        list_17.append(i ** 3 + 17)

total_sum = 0
total_sum_17 = 0
for el in my_list:
    sum_el = 0
    n = el
    while n > 0:
        sum_el += (n % 10)
        n //= 10
    if sum_el % 7 == 0:
        total_sum += el
for el in list_17:
    sum_el_17 = 0
    n = el
    while n > 0:
        sum_el_17 += (n % 10)
        n //= 10
    if sum_el_17 % 7 == 0:
        total_sum_17 += el


print(f' Сумма чисел, сумма цифр которых делится на 7 равна {total_sum}')
print(f' Сумма чисел, увеличенных на 17, сумма цифр которых делится на 7 равна {total_sum_17}')
