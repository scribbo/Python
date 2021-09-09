numbers = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
           'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(key):
    if key.istitle() == True:
        print(numbers.get(key.lower()).title())
    else:
        print(numbers.get(key.lower()))


num_translate(input('Введите числительное от 0 до 10: '))