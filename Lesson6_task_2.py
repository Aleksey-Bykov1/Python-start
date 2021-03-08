"""
    В программе сначала создается список только ip адресов,
    затем создается множество чтобы убрать повторы.
    А потом по значениям множества находиться наибольшее колличество запросов
    с одного адреса через спосок line_3.
"""

with open('nginx_logs.txt', 'r', encoding='utf-8') as logs:
    line_3 = []
    for line in logs:
        line_1 = line.replace('-', '').replace('"', '').split()
        line_3.append(f'{line_1[0]}')
st = set(line_3)
max_cou = 0
spammer = ''
for i in st:
    count = line_3.count(i)
    if count > max_cou:
        max_cou = count
        spammer = i
print(f' Данный IP адрес авляется спамером -> {spammer}, с колличеством запросов: {max_cou}')





