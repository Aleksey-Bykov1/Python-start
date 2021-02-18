def thesaurus(*args):
    di = {}
    for i in args:
        if i[0] in di:
            di[i[0]] += [i]
        else:
            di[i[0]] = [i]
    return print(di)


thesaurus("Иван", "Мария", "Петр", "Илья")
