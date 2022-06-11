# 1.
import datetime
class Data:

    def __init__(self, data):
        self.data = data

    @classmethod
    def data_int(cls, data):
        if len(data) == 10 and data[2] == '-' and data[5] == '-':
            try:
                num = int(data.split('-')[0])
                month = int(data.split('-')[1])
                year = int(data.split('-')[2])
            except ValueError:
                print('Неверный формат даты')
            except TypeError:
                print('Неверный формат даты')
            else:
                return num, month, year
        else:
            print('Неверный формат даты')

    @staticmethod
    def check_data(num, month, year):
        try:
            datetime.date(year, month, num)
        except ValueError:
            print('Недопустимые значения для даты')
        except TypeError:
            print('Недопустимые значения для даты')
        else:
            print('Значения даты соответствуют допустимым')

d = Data(input('Введите дату в формате дд-мм-гггг: '))
print(Data.data_int(d.data))
d.check_data(Data.data_int(d.data)[0], Data.data_int(d.data)[1], Data.data_int(d.data)[2])
d.check_data(12, 10, 2000)

# 2.
class ExceptZero(Exception):
    def __init__(self, txt):
        self.txt = txt

try:
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    if b == 0:
        raise ExceptZero('Нельзя делить на ноль')
except (ValueError, ExceptZero) as err:
    print(err)
else:
    print(f'Ответ {a/b}')

# 3.
class ListNum(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []
while True:
    try:
        el = input('Введите число: ')
        if el == 'stop':
            break
        else:
            for i in el:
                if i not in ['0','1','2','3','4','5','6','7','8','9','.']:
                    raise ListNum('Список должен состоять из чисел')
    except ListNum as err:
        print(err)
    else:
        my_list.append(el)
print(my_list)

# 4, 5, 6.
import copy

class NumNotInt(Exception):
    def __init__(self, txt):
        self.txt = txt

class Warehouse:
    def __init__(self, wh_capasity, dep_capacity):
        self.wh_capacity = wh_capasity #вместимость склада
        self.dep_capacity = dep_capacity #техника, необходимая подразделениям
        self.wh_filled_place = {} #количество и характеристики техники, передаваемой на склад
        self.wh_filled_place_sum = 0 #общее количество техники, передаваемой на склад
        self.wh_free_place_sum = wh_capasity #свободные места на складе
        self.wh_list = [] #список техники на складе
        self.dep_list = [] #список техники в подразделениях
        self.wh_list_sum = 0# количество техники на складе
        self.dep_list_sum = 0  # количество техники, переданной в подразделения, всего

    def wh_fill(self, *off_equip):
        """поступление техники на склад, принимает объекты офисной техники
        Формирует словарь с ключами принтер, сканер, ксерокс и списком количества и характеристик объектов оргтехники,
        поступившими на склад, также считает сколько единиц техники всего на складе, формирует список хранящейся
        на складе техники исходя из предыдущих поступлений"""
        for el in off_equip:
            if type(el) is Printer:
                self.wh_list.append(['Принтер', el.my_list()])
            elif type(el) is Scaner:
                self.wh_list.append(['Сканер', el.my_list()])
            else:
                self.wh_list.append(['Ксерокс', el.my_list()])
            self.wh_filled_place['Принтер'] = [el.my_list() for el in off_equip if type(el) is Printer]
            self.wh_filled_place['Сканер'] = [el.my_list() for el in off_equip if type(el) is Scaner]
            self.wh_filled_place['Ксерокс'] = [el.my_list() for el in off_equip if type(el) is not Printer and type(el) is not Scaner]
        list_num1 = [self.wh_filled_place[i] for i in self.wh_filled_place.keys()] #форматирование списков списков для сложения количества
        list_num2 = list_num1[0] + list_num1[1] + list_num1[2] #форматирование списков списков для сложения количества
        list_num3 = [list_num2[i][0] for i in range(0, len(list_num2))] #форматирование списков списков для сложения количества
        self.wh_filled_place_sum = sum(list_num3)#количество передаваемой на склад техники
        wh_list1 = [self.wh_list[i][1][0] for i in range(0, len(self.wh_list))]
        self.wh_list_sum = sum(wh_list1)
        return self.wh_filled_place, self.wh_filled_place_sum, self.wh_list, self.wh_list_sum

    @property
    def wh_fill_type(self): #техника, передаваемая на склад по типам
        wh_filled_type_dict = {key: [self.wh_filled_place[key][i][0] for i in range(0, len(self.wh_filled_place[key]))] for key in self.wh_filled_place.keys()}
        wh_filled_type = {key: sum(wh_filled_type_dict[key]) for key in wh_filled_type_dict.keys()}
        return wh_filled_type

    def dep_fill(self, dep, off_equip, num): #поступление техники в подразделения
        """принимает подразделение, объект оффисной техники, его количество, возвращает список с описанием количества
        и характеристик техники, переданной в подразделения, а также уменьшает количество этой техники на складе, возвращает список
        техники, оставшейся на складе, а также общее количество единиц,
         переданных в подразделение и оставшихся на складе"""
        my_list1 = copy.deepcopy(off_equip.my_list())
        try:
            my_list1[0] = num
            if type(num) is not int:
                raise NumNotInt('Количество техники введено в строковом формате, необходим формат целого числа')
        except (ValueError, NumNotInt) as err:
            print(err)
        else:
            if type(off_equip) is Printer:
                self.dep_list.append([dep, 'Принтер', my_list1])
            elif type(off_equip) is Scaner:
                self.dep_list.append([dep, 'Сканер', my_list1])
            else:
                self.dep_list.append([dep, 'Ксерокс', my_list1])
            dep_list1 = [self.dep_list[i][2][0] for i in range(len(self.dep_list))]
            self.dep_list_sum = sum(dep_list1)
            for el in self.wh_list:
                if el[1][1:] == self.dep_list[len(self.dep_list)-1][2][1:]:
                    el[1][0] = el[1][0] - num
            wh_list1 = [self.wh_list[i][1][0] for i in range(0, len(self.wh_list))]
            self.wh_list_sum = sum(wh_list1)
            return self.dep_list, self.dep_list_sum, self.wh_list, self.wh_list_sum

    @property
    def wh_free(self):
        self.wh_free_place_sum = self.wh_capacity - self.wh_list_sum
        return self.wh_free_place_sum

    @property
    def dep_dict(self):#количество техники в подразделениях по типу
        dep_dict = {}
        dep_dict['one'] = {el[1]: sum([el[2][0]]) for el in self.dep_list if el[0] == 'one'}
        dep_dict['two'] = {el[1]: sum([el[2][0]]) for el in self.dep_list if el[0] == 'two'}
        return dep_dict

    def __str__(self):
        return f'Склад на {self.wh_capacity} мест хранения, на складе {self.wh_list_sum} единиц оргтехники, свободных мест складе: {self.wh_free}'

from abc import ABC, abstractmethod

class AbcOfficeEquipment(ABC):
    @abstractmethod
    def age(self, this_year):
        pass

class OfficeEquipment(AbcOfficeEquipment):
    def __init__(self, number, model, company, year, price):
        self.number = number
        self.model = model
        self.company = company
        self.__year = year
        self.price = price

    def my_list(self):
        return [self.number, self.model, self.company, self.year, self.price]

    def __str__(self):
        return f'Оффисная техника, производство {self.company} модель {self.model}, год выпуска {self.year}, цена закупки {self.price}, количество {self.number} шт'

    def __add__(self, other):
        if self.my_list()[1:] == other.my_list()[1:]:
            return OfficeEquipment(self.my_list()[0]+other.my_list()[0], self.my_list()[1], self.my_list()[2], self.my_list()[3], self.my_list()[4])
        else:
            print('Нельзя сложить объекты с разными характеристиками')

    def age(self, this_year): #возраст объекта
        return this_year - self.year

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new):
        if new > 2022:
            self.__year = 2022
        elif new < 2018:
            self.__year = 2018
        else:
            self.__year = new

class Printer(OfficeEquipment):

    def __init__(self, number, model, company, year, price, color=None):
        super().__init__(number, model, company, year, price)
        self.color = color

    def my_list(self):
        return [self.number, self.model, self.company, self.year, self.price, self.color]

    def __add__(self, other):
        if self.my_list()[1:] == other.my_list()[1:]:
            return Printer(self.my_list()[0] + other.my_list()[0], self.my_list()[1], self.my_list()[2], self.my_list()[3], self.my_list()[4], self.my_list()[5])
        else:
            print('Нельзя сложить объекты с разными характеристиками')

    def __str__(self):
        return f'Принтер {self.my_list()[2]} модели {self.my_list()[1]} год выпуска {self.my_list()[3]}, цена {self.my_list()[4]}, количество {self.my_list()[0]}'

    def color_print(self):
        if self.color is not None:
            return 'Возможна цветная печать.'
        else:
            return 'Печать только черно-белая.'

class Scaner(OfficeEquipment):

    def __init__(self, number, model, company, year, price, size):
        super().__init__(number, model, company, year, price)
        self.size = size

    def my_list(self):
        return [self.number, self.model, self.company, self.year, self.price, self.size]

    def __add__(self, other):
        if self.my_list()[1:] == other.my_list()[1:]:
            return Scaner(self.my_list()[0] + other.my_list()[0], self.my_list()[1], self.my_list()[2], self.my_list()[3], self.my_list()[4], self.my_list()[5])
        else:
            print('Нельзя сложить объекты с разными характеристиками')

    def __str__(self):
        return f'Сканер {self.my_list()[2]} модели {self.my_list()[1]} год выпуска {self.my_list()[3]}, цена {self.my_list()[4]}, количество {self.my_list()[0]}'

    def size_scan(self):
        return 'Сканирует только А4' if self.size == 'А4' else 'Сканирует А3 и А4'

class Xerox(OfficeEquipment):

    def __init__(self, number, model, company, year, price, num_copies):
        super().__init__(number, model, company, year, price)
        self.num_copies = num_copies

    def my_list(self):
        return [self.number, self.model, self.company, self.year, self.price, self.num_copies]

    def __add__(self, other):
        if self.my_list()[1:] == other.my_list()[1:]:
            return Xerox(self.my_list()[0] + other.my_list()[0], self.my_list()[1], self.my_list()[2], self.my_list()[3], self.my_list()[4], self.my_list()[5])
        else:
            print('Нельзя сложить объекты с разными характеристиками')

    def __str__(self):
        return f'Ксерокс {self.my_list()[2]} модели {self.my_list()[1]} год выпуска {self.my_list()[3]}, цена {self.my_list()[4]}, количество {self.my_list()[0]}'

print('Формирование объектов техники')
p1 = Printer(5, 'm2', 'philips', 2021, 15000, 'color')
p2 = Printer(7, 'm3', 'philips', 2021, 15000, 'color')
p3 = p1 + p2
print(p1.my_list())
print(p2.my_list())
p4 = Printer(3,'m2', 'philips', 2021, 15000, 'color')
print(p4.my_list())
p5 = p1 + p4
print(p5.my_list())
print(f'{p5}. {p5.color_print()}')

s1 = Scaner(5, 'AMA320', 'Panasonic', 2020, 20000, 'A4')
s2 = Scaner(15, 'AMA320', 'Panasonic', 2020, 20000, 'A4')
s3 = Scaner(15, 'AMA320', 'Panasonic', 2020, 20000, 'A3, A4')
s4 = s1 + s2
print(f' {s4}. {s4.size_scan()}')
print(s4.my_list())

x1 = Xerox(10, 'DDS200', 'Xerox', 2020, 50000, 20)
x2 = Xerox(2, 'DDS230', 'Xerox', 2019, 52000, 30)
x3 = x1 + x2
print(x1.my_list())
x1.year = 2028
print(x1.year)
print(x1)
print(x1.my_list())
print('Работа склада:')
w1 = Warehouse(100, {'one':{'Принтер':5, 'Сканер': 2, 'Ксерокс': 1}, 'two':{'Принтер': 1, 'Сканер': 5, 'Ксерокс': 10}})
print(w1)
print(f'Всего подразделениям "one" и "two" необходимо: {w1.dep_capacity}')
w1.wh_fill(p1, p2, s1, s2, x1, x2)
print(f'На склад поступила оргтехника: {w1.wh_filled_place}.\nВсего поступило {w1.wh_filled_place_sum} единицы.\nНа складе хранится техника: {w1.wh_list}')
print(w1)
print(f'Поступила техника по типам (шт): {w1.wh_fill_type}')
w1.dep_fill("one", p1, 1)
print(f'В подразделение {w1.dep_list[len(w1.dep_list)-1][0]} передана техника {w1.dep_list[len(w1.dep_list)-1][1:]}')
print(w1)
print(w1.wh_list)
w1.dep_fill("two", p1, 1)
print(f'В подразделение {w1.dep_list[len(w1.dep_list)-1][0]} передана техника {w1.dep_list[len(w1.dep_list)-1][1:]}, \nв подразделениях на данный момент находится следующая техника: {w1.dep_list[0][0]}:{w1.dep_list[0][1:]}, \n{w1.dep_list[1][0]}:{w1.dep_list[1][1:]}')
print(w1)
print(w1.wh_list)
w1.dep_fill('one', s1, '1')
print(w1.dep_list)
print(f'Всего техники в подразделениях: {w1.dep_list_sum} шт')
print(w1)
print(w1.wh_list)
print(w1.wh_free)
print(w1.dep_dict)

#7.
#a + bi + c +di = а+с + (b+d)
#(ac - bd)+(ad + bc)i

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return Complex(self.a + other.a, self.b+other.b)
    def __mul__(self, other):
        return Complex(self.a*other.a - self.b*other.b, self.a*other.b + self.b*other.a)
    def __str__(self):
        return f'Комплексное число {self.a} + {self.b}*i, где i**2 = -1'

c = Complex(2, 3)
print(c)
d = Complex(4, 5)
print(d)
my_sum = c + d
print(my_sum)
my_mul = c * d
print(my_mul)
