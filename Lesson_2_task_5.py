price_list = [57.8, 46.51, 97, 314, 73, 211.03, 1678.22, 84, 90, 74.9, 3407, 94]
new_price_list = []
one_price = []

# вывожу на экран цену .. рублей .. копеек
for ind, var in enumerate(price_list):
    new_price_list.append(str(var / 1))
for i in new_price_list:
    one_price = i.split('.')
    print(one_price[0], 'руб', one_price[1].zfill(2), 'коп' + ', ', end='')

print('\n')

# вывожу исходный прайс лист до сортировки, отсортитованный и сново исходный, показывая что он не изменился
print('Исходный список -> ', price_list, '\n')
print('По возрастанию ->', sorted(price_list), '\n')
print('Исходный список -> ', price_list, '\n')

# создаю новый список и сортирую по убыванию
new_sort_price = sorted(price_list)
new_sort_price = new_sort_price[::-1]
print('По убыванию ->', new_sort_price, '\n')

# цены пяти самых дорогих товаров
print('Пять самых дорогих ->', new_sort_price[0:5])
