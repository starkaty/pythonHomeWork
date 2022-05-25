from functools import reduce
from sys import argv
from itertools import count, cycle
from math import factorial

#1

def salary(hours, rate, bonus):
    return hours * rate + bonus

print(salary(float(argv[1]), float(argv[2]), float(argv[3])))

#2
list1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list2 = [list1[i] for i in range(1, len(list1)) if list1[i] > list1[i-1]]
print(list2)

#3
my_list = [i for i in range(20, 241) if i % 20 == 0 or i % 21 ==0]
print(my_list)

#4
list1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
list2 = [el for el in list1 if list1.count(el) == 1]
print(list2)

#5
def mult(a, b):
    return a * b

my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(my_list)
print(reduce(mult, my_list))

#6
for el in count(3, 1):
    print(el)
    if el > 9:
        break

n = 0
for el in cycle('Hello, how are you?'):
    print(el)
    if n > 20:
        break
    n += 1

#7

def fact(n):
    for i in range(1, n+1):
        yield factorial(i)

gen_fact = (fact(int(input('Введите число n: '))))
print(gen_fact)

for el in gen_fact:
    print(el)







