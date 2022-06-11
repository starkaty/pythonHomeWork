#1
def div(a,b):
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        print('Число b не может быть равно 0')
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
print(div(a, b))

#2
def my_name(name = 'данные отсутствуют', surname = 'данные отсутствуют', birth_year = 'данные отсутствуют', city = 'данные отсутствуют', email = 'данные отсутствуют', phone = 'данные отсутствуют'):
    print(f'Имя: {name}, Фамилия: {surname}, год рождения: {birth_year}, город проживания: {city}, адрес электронной почты: {email}, телефон: {phone}.')

my_name(name='Darya', surname='Ivanova', birth_year='1996', city='Moscow', email='iv@yandex.ru', phone='123456')
my_name(name = 'Maria')

#3
def my_func(a, b, c):
    my_list = [a, b, c]
    max1 = max(my_list)
    my_list.remove(max1)
    max2 = max(my_list)
    return max2 + max1
print(my_func(100, 200, 500))

#4 (1) функция работает для любых значений у
def degree(x, y):
    res = x ** y
    return res
print(degree(int(input('Введите положительное целое число x: ')), int(input('Введите целое число y: '))))

#4 (2) функция реализована для любых значений у
def degree(x, y):
    res = 1
    if y<0:
        for i in range(y, 0):
            res = res * 1/x
    elif y>0:
        for i in range(0, y):
            res = res * x
    else:
        res = 1
    return res
print(degree(int(input('Введите положительное целое число x: ')), int(input('Введите целое число y: '))))

#5
def my_sum():
    """Функция рассчитывает сумму введенных пользователем через пробел чисел до тех пор, пока не будет введен символ 'q',
    каждый раз при нажатии клавиши 'enter' происходит расчет суммы с учетом ранее полученного результата,
    если символ 'q' введен после ряда чисел в одной строке, то числа, стоящие в строке до 'q', также будут учтены в расчете"""
    numbers_sum = 0
    while True:
        numbers = input('Введите числа через пробел либо введите q для выхода из программы: ').split()
        if 'q' in numbers:
            if numbers == ['q']:
                break
            else:
                ind = numbers.index('q')
                numbers_list = [int(num) for num in numbers[0:ind]]
                numbers_sum = sum(numbers_list) + numbers_sum
                print(numbers_sum)
                break
        else:
            numbers_list = [int(num) for num in numbers]
            numbers_sum = sum(numbers_list) + numbers_sum
            print(numbers_sum)
my_sum()

#6, #7
def int_func(text):
    if text.lower() == text:
        res = text.title()
        return res
    else:
        print('В данной строке не все буквы в нижнем регистре')

print(int_func(input('Введите слово или строку (все буквы должны быть в нижнем регистре): ')))
















