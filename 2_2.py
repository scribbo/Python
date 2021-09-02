my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
my_list_new = []

for i in range(len(my_list)):
    a = my_list[i][1:]

    if my_list[i].isdigit():
        my_list_new.append(f'"{int(my_list[i]):02d}"')
    elif my_list[i][0] == '+' and a.isdigit():
        my_list_new.append(f'"+{int(a):02d}"')
    elif my_list[i][0] == '-' and a.isdigit():
        my_list_new.append(f'"-{int(a):02d}"')
    else:
        my_list_new.append(my_list[i])

print(' '.join(my_list_new))
