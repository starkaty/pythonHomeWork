#1
name = 'Katya'
age = 39
city = 'Moscow'
print(f'My name is {name}, I`m {age}, I live in {city}.')

name1 = input('Your name: ')
age1 = int(input('How old are you: '))
city1 = input('Your City: ')
print(f'Your name is {name1}, you are {age1}, you live in {city1}.')

#2
time_sec = int(input('Введите время в секундах: '))
hour = time_sec//3600
min = (time_sec - hour*3600)//60
sec = time_sec - hour*3600 - min*60
print(f'time {str(hour).zfill(2)}:{str(min).zfill(2)}:{str(sec).zfill(2)}')

#3
n = input('Введите число n: ')
sum_n = int(n) + int(n+n) + int(n+n+n)
print(sum_n)

#4
num = int(input('Введите целое положительное число: '))
last = 0
while num > 0:
    if last <= num % 10:
        last = num % 10
    num = num // 10
print(f'Max: {last}')

#5
earn = float(input('Введите выручку: '))
costs = float(input('Введите издержки: '))
if earn > costs:
    print('Вы получили прибыль')
elif earn == costs:
    print('Ваши доходы равны расходам')
else:
    print('У вас убыток')

#6
if earn > costs:
    profitability = round((earn - costs)/earn, 4)
    print(f'Ваша рентабельность составила {profitability}, (в процентах: {round(((earn - costs)/earn)*100, 2)}%)')
    num_staff = int(input('Введите численность сотрудников: '))
    one_emp_prof = round((earn - costs)/num_staff, 2)
    print(f'Прибыль в расчете на одного сотрудника составила {one_emp_prof}')

#7
a = float(input('Введите результат в первый день (а): '))
b = float(input('Введите результат, который необходимо превзойти (b): '))
day = 1
while a < b:
    a = a * 1.1
    day += 1
print(f'На {day} день спортсмен достиг результата не менее {b} км.')













