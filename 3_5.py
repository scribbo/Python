from random import randrange, choice


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


"""
def get_jokes(n, repeat):
    if repeat.lower() == 'yes':
        i = 0
        while i < n:
            print(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
            i += 1

    else:
        i = 0
        while i < n:
            print(f'{nouns.pop(randrange(len(nouns)))} {adverbs.pop(randrange(len(adverbs)))} {adjectives.pop(randrange(len(adjectives)))}')
            i += 1

get_jokes(repeat = 'no', n = 4)
"""
