#1
my_list_1 = [1, 'hello', [1,2,3], True, 1.25, {'one', 'two', 'three'}, {'one':1, 'two':2, 'three':3}, ('hello', 'my', 'friend'), b'hello']
for i in my_list:
    print(type(i), ': ',i)

#2
my_list_2 = [input('Введите элемент списка: ') for i in range(0, int(input('Введите длину списка: ')))]
print(my_list_2)
if len(my_list_2) % 2 == 0:
    for i in range(0, len(my_list_2)):
        if i % 2 == 0:
            my_list_2[i], my_list_2[i+1] = my_list_2[i+1], my_list_2[i]
else:
    for i in range(0, len(my_list_2)-1):
        if i % 2 == 0:
            my_list_2[i], my_list_2[i+1] = my_list_2[i+1], my_list_2[i]
print(my_list_2)

#3 (list)
month = int(input('Введите месяц: '))
month_number = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
if month in month_number[0:3]:
    print('Зима')
elif month in month_number[3:6]:
    print('Весна')
elif month in month_number[6:9]:
    print('Лето')
else:
    print('Осень')

#3 (dict)
month = int(input('Введите месяц: '))
month_season = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
for m in month_season:
    if month in month_season[m]:
        print(m)
        break

#4
my_str = input('Введите строку: ')
my_str_list = my_str.split()
for i, el in enumerate(my_str_list, 1):
    print(i, el[0:10])

#5
my_list = [7, 5, 3, 3, 2]
new_el = int(input('Введите новый элемент рейтинга: '))
for i in range(0, len(my_list)):
    if my_list[i] < new_el:
        my_list.insert(i, new_el)
        break
    elif my_list[i] == new_el:
        my_list.insert(i+my_list.count(new_el), new_el)
        break
    elif my_list[len(my_list)-1] > new_el:
        my_list.insert(len(my_list), new_el)
        break
print(my_list)

#6
list_product = [input('Введите через пробел название товара, его цену, количество и меру измерения количества (шт или кг): ') for i in range(0, int(input('Введите количество наименованмй товаров, которые будут проанализированы: ')))]
list_product_1 = [el.split() for el in list_product]
names = ['название', 'цена', 'количество', 'ед']
dict_product = [(el+1, {names[0]:list_product_1[el][0], names[1]:float(list_product_1[el][1]), names[2]:int(list_product_1[el][2]), names[3]:list_product_1[el][3]}) for el in range(0, len(list_product_1))]
print(dict_product)
dict_for_an = {names[0] : list(set([el[0] for el in list_product_1])), names[1] : list(set([el[1] for el in list_product_1])), names[2] : list(set([el[2] for el in list_product_1])), names[3] : list(set([el[3] for el in list_product_1]))}
print(dict_for_an)
