from itertools import zip_longest
from json import dump

with open('users.csv', 'r', encoding='utf-8') as f_users:
    name = f_users.read()
    names = name.split('\n')

with open('hobby.csv', 'r', encoding='utf-8') as f_hobby:
    hobby = f_hobby.read()
    hobbies = hobby.split('\n')

new = {k.replace(',', ' '): n if len(names) >= len(hobbies) else exit(1) for k, n in zip_longest(names, hobbies, fillvalue=None)}

with open('my_dict.json', 'w', encoding='utf-8') as f_dict:
    dump(new, f_dict, ensure_ascii=False, indent=5)
    print(new)
