# Вызываю функцию choice из модуля random
from random import choice

# Наполняю списки значениями
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

""" Создаю фукцию get_jokes  возвращающую "num" шуток, сформированных из трех случайных слов, 
взятых из трёх списков (по одному из каждого. Для отключения повторов слов необходимо указать 
параметр repeat = False для включения repeat = True. По умолчанию repeat = False."""


def get_jokes(num, repeat=False):
    li = []
    li_2 = []
    if repeat == True:
        for i in range(num):
            jok = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
            li.append(jok)
    elif repeat == False:
        while len(li) != (num * 3):
            jok_nouns = choice(nouns)
            jok_adverbs = choice(adverbs)
            jok_adjectives = choice(adjectives)
            if jok_nouns not in li and jok_adverbs not in li and jok_adjectives not in li:
                li.extend([jok_nouns, jok_adverbs, jok_adjectives])
                li_2.append(f'{jok_nouns} {jok_adverbs} {jok_adjectives}')

    if repeat == True:
        return print(li)
    elif repeat == False:
        return print(li_2)


# Вызываю фукцию get_jokes с параметрами
get_jokes(3, repeat=False)
