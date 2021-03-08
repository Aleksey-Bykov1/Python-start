from sys import argv

with open('bakery.csv', 'r', encoding='utf-8') as f:
    line = f.readline()
    index = []
    index.append(line.strip())
    while line:
        line = f.readline()
        index.append(line.strip())
    index.pop()


def show_sale(start=1, stop=len(index)):
    for i in range(start - 1, stop):
        print(index[i])

if len(argv) == 1:
    show_sale()
elif len(argv) == 2:
    show_sale(int(argv[1]))
else:
    show_sale(int(argv[1]), int(argv[2]))
