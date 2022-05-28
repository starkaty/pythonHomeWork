import math
import json

#1. Создать программный файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

with open('hw_lesson05_1.txt', 'w', encoding='utf-8') as f:
    while True:
        new_info = input('Введите строку: ')
        if new_info == '':
            break
        else:
            f.write(new_info+'\n')

#2. Создать текстовый файл (не программно),
# сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке.

with open('hw_lesson05_2.txt', 'w', encoding='utf-8') as f: #файл создан не программно, информация записана в него программно
    f.writelines(['hello\n', 'how are you\n', 'hello world\n', 'here is my friend\n'])

with open('hw_lesson05_2.txt', 'r', encoding='utf-8') as f:
    print('Количество строк: ' + str(len(f.readlines())))
    f.seek(0)
    lines = f.readlines()
    for i in range(1, len(lines)+1):
        print('Количество слов в строке ', i, '-', len(lines[i-1].split()), 'шт.')

#3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников
#и величину их окладов (не менее 10 строк).
#Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
#Выполнить подсчёт средней величины дохода сотрудников.

with open('hw_lesson05_3.txt', 'w', encoding='utf-8') as f: #файл создан не программно, информация в него записана программно
    f.writelines(['Иванов 10000.15\n', 'Петров 20000.22\n', 'Сидоров 15000.55\n', 'Андреев 40000.65\n', 'Алексев 13000.45\n', 'Смирнов 60000.63\n', 'Савельев 70000.32\n', 'Николаев 80000.21\n', 'Павлов 90000.65\n', 'Федоров 65000.65\n', 'Александров 75000.55\n' ])

with open('hw_lesson05_3.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    lines_dict = {lines[i].split()[0] : float(lines[i].split()[1]) for i in range(0, len(lines))}
    for key in lines_dict.keys():
        if lines_dict[key] < 20000:
            print(key + ' имеет оклад менее 20000')
    lines_num = [lines_dict[key] for key in lines_dict.keys()]
    lines_num_av = math.fsum(lines_num)/len(lines_num)
    print('Средняя величина дохода (если допустить, что оклад равен доходу) равна: ', round(lines_num_av, 2))

#4 Создать (не программно) текстовый файл с содержимым
#Напишите программу, открывающую файл на чтение и считывающую построчно данные.
#При этом английские числительные должны заменяться на русские.
#Новый блок строк должен записываться в новый текстовый файл.

dict_num = {'one' : 'один', 'two' : 'два', 'three' : 'три', 'four' : 'четыре'} #создаем словарь перевода числительных на русский
with open('hw_lesson05_4old.txt', 'r', encoding='utf-8') as f: #открываем файл для чтения (в нем уже записаны данные)
    lines = f.readlines() # сохраняем список строк в переменную
lines_dict = {lines[i].split(' - ')[0] : lines[i].split(' - ')[1] for i in range(0, len(lines))} #из списка строк создаем словарь, чтобы отделить число от числительного
lines_dict_new = {dict_num[key.lower()].title():lines_dict[key] for key in lines_dict.keys()} #создаем новый словарь, где английское числительное меняется на русское

with open('hw_lesson05_4new.txt', 'w', encoding='utf-8') as f: #создаем и открываем новый файл на запись
    f.writelines([' - '.join([key, lines_dict_new[key]]) for key in lines_dict_new.keys()]) #записываем данные в файл, "склеив" ключи и значения словаря, превратив его в список для записи строк

#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
#Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open('hw_lesson05_5.txt', 'w+', encoding='utf-8') as f:
    f.write('10 20 30 40.56 50 60 70 80 90 100\n')
    f.seek(0)
    my_line = f.read().split()
my_line_float = [float(el) for el in my_line] #переводим каждое значение списка в формат числа float
print('Сумма чисел в файле ', round(sum(my_line_float), 2))

# 6. Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет
# и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.

ascii_numbers = [i for i in range(48, 58)]#для поиска цифр в строке применим ascii таблицу

with open('hw_lesson05_6.txt', 'r', encoding='utf-8') as f:
    my_list = f.readlines() #создаем список строк из файла

my_list_dict = {my_list[i].split(':')[0]:my_list[i].split(':')[1]  for i in range(0, len(my_list))} #создаем словарь, отделяем название предмета - ключ по принципу наличия ":"

for key in my_list_dict.keys():
    my_list_dict[key] = ''.join([el if ord(el) in ascii_numbers or ord(el) == 32 else '' for el in my_list_dict[key]]).split() # убираем все символы из значения в словаре, кроме пробелов и цифр, получаем список
    my_list_dict[key] = [int(el) for el in my_list_dict[key]] #приводим элементы списка к формату int для суммирования

my_list_dict_new = {key: sum(my_list_dict[key]) for key in my_list_dict.keys()} #формируем словарь

print(my_list_dict_new)

#7

with open('hw_lesson05_7.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines() #прочитали строки файла, сохранили в переменную

lines_s = [el.split() for el in lines] # каждую строку перевели в формат списка (принцип разделения: " "), чтобы далее разделить значения
lines_s_dict = {lines_s[k][0] : [float(lines_s[k][i]) for i in range(2,4)] for k in range(0, len(lines_s))} # создали словарь, оставив только фирму, выручку и издержки (в формате float)
lines_s_dict_profit = {key: round(lines_s_dict[key][0]-lines_s_dict[key][1], 2) for key in lines_s_dict.keys()} # создали словарь фирма - прибыль(убыток)
av_profit_dict = [lines_s_dict_profit[key] for key in lines_s_dict_profit.keys() if lines_s_dict_profit[key] >=0] #создали список для расчета средней прибыли
av_profit = round(sum(av_profit_dict)/len(av_profit_dict), 2) #рассчитали среднюю прибыль

profit_list = [lines_s_dict_profit, {'average_profit':av_profit}] #формируем список фирма-прибыль(убыток), средняя прибыль (исключая фирмы с убытками)
print(profit_list)

with open('hw_lesson05_7.json', 'w', encoding='utf-8') as f:
    json.dump(profit_list, f)





