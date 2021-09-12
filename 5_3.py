from itertools import zip_longest
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Илья', 'Харитон'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


new = [(k, n) for k, n in zip_longest(tutors, klasses)]

print(*new)