import os
from collections import defaultdict

import django

root_dir = django.__path__[0]
django_files = defaultdict(int)
size_list_new = []
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if os.stat(os.path.join(root, file)).st_size < 100:
            size_list_new.append('100')
        elif 100 <= os.stat(os.path.join(root, file)).st_size < 1000:
            size_list_new.append('1000')
        elif 1000 <= os.stat(os.path.join(root, file)).st_size < 10000:
            size_list_new.append('10000')
        else:
            size_list_new.append('100000')

for el in size_list_new:
    django_files[el] += 1

for key, value in sorted(django_files.items()):
    print(f'{key}: {value}')