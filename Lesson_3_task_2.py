translator = {
    'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
    'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'
}


def num_translate_adv(*args):
    if str(args).istitle():
        args = ' '.join(args).lower()
        values = translator.get(args)
        return print(values.title())
    else:
        return print(translator.get(*args))


num_translate_adv('Seven')

