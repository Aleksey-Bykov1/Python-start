tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Антон', 'Василий'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

if len(tutors) == len(klasses):
    result = (tuple((f'{tutors[i]} {klasses[i]} '.split())) for i in range(len(tutors)))
else:
    for i in range(len(tutors) - len(klasses)):
        klasses.append(None)
    result = (tuple((f'{tutors[i]} {klasses[i]} '.split())) for i in range(len(tutors)))
print(type(result), *result, sep='\n')
