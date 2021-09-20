from itertools import zip_longest
from json import dump

with open('users.csv', 'r', encoding='utf-8') as f_users:
    with open('hobby.csv', 'r', encoding='utf-8') as f_hobby:
        us_hobby = zip_longest(f_users, f_hobby, fillvalue=None)

        with open('my_dict.txt', 'w', encoding='utf-8') as f_dict:
            for el in us_hobby:
                print(f"{str(el[0]).strip().replace(',', ' ')}: {str(el[1]).strip()}", file=f_dict)
