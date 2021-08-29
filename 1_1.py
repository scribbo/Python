time = int(input('Введите время в секундах: '))

s = time % 60
m = (time // 60) % 60
h = (time % 86400) // 3600
d = time // 86400
if 0 <= time < 60:
    print(f'{time} сек = {s} сек')
elif 60 <= time < 3600:
        print(f'{time} сек = {m} мин {s} сек')
elif 3600 <= time < 86400:
        print(f'{time} сек =  {h} ч {m} мин {s} сек')
elif time >= 86400:
        print(f'{time} сек = {d} дн {h} ч {m} мин {s} сек')
else:
    print('Введите положительное число')



