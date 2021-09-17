from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as f_users:
    name = f_users.read()
    names = name.split('\n')


with open('hobby.csv', 'r', encoding='utf-8') as f_hobby:
    hobby = f_hobby.read()
    hobbies = hobby.split('\n')


new = {k.replace(',', ' '): n if len(names) >= len(hobbies) else exit(1) for k, n in zip_longest(names, hobbies)}

print(new)
