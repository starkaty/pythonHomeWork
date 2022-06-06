# 1
class Matrix:
    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __str__(self):
        my_list = ['  '.join(self.my_matrix[i]) for i in range(0, len(self.my_matrix))]
        return '\n'.join(my_list)

    def __add__(self, other):
        if len(self.my_matrix[0]) == len(other.my_matrix[0]) and len(self.my_matrix) == len(other.my_matrix):
            my_matrix_add = [
                [str(int(self.my_matrix[j][i]) + int(other.my_matrix[j][i])).rjust(5) for i in range(0, len(self.my_matrix[0]))]
                for j in range(0, len(self.my_matrix))]
            return Matrix(my_matrix_add)
        else:
            return 'Складываемые матрицы должны иметь одинаковый размер'

my_matrix1 = [[input('Введите значение матрицы: ').rjust(5) for i in range(0, 4)] for j in range(0, 3)]
m1 = Matrix(my_matrix1)
print(m1.my_matrix)
print(m1)

my_matrix2 = [[input('Введите значение матрицы: ').rjust(5) for i in range(0, 4)] for j in range(0, 3)]
m2 = Matrix(my_matrix2)
print(m2.my_matrix)
print(m2)

my_matrix3 = [[input('Введите значение матрицы: ').rjust(5) for i in range(0, 4)] for j in range(0, 3)]
m3 = Matrix(my_matrix3)
print(m3.my_matrix)
print(m3)

print(f'Сумма двух матриц:\n{m1 + m2}')

print(f'Сумма трех матриц:\n{m1 + m2 + m3}')

# 2
from abc import ABC, abstractmethod


class Abcclothes(ABC):
    @abstractmethod
    def fab_consump(self):
        pass


class Clothes(Abcclothes):

    def __init__(self, size=0, num_size=0, height=0, num_height=0, year=2022):
        """Считает общий расход ткани по росту или размеру для производства одежды.
            Принимает аргументы: размер и количество единиц одежды для расчета по размеру (как пальто),
            рост и количество единиц для расчета по росту (как костюм), год"""
        self.num_size = num_size
        self.num_height = num_height
        self.size = size
        self.height = height
        self.__year = year

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new):
        if new > 2022:
            self.__year = 2022
        elif new < 2019:
            self.__year = 2019
        else:
            self.__year = new

    def __str__(self):
        if self.size == 0:
            if self.height == 0:
                return 'Данные отсутствуют'
            else:
                return f'Расход ткани на одежду ' \
                       f'(по росту {self.height} сшито {self.num_height} ед.) ' \
                       f'составляет {self.fab_consump()}'
        elif self.height == 0:
            return f'Расход ткани на одежду ' \
                   f'(по размеру {self.size} сшито {self.num_size} ед.), ' \
                   f'составляет {self.fab_consump()}'
        else:
            return f'Расход ткани на одежду ' \
                   f'(по размеру {self.size} сшито {self.num_size} ед., ' \
                   f'по росту {self.height} сшито {self.num_height} ед.) ' \
                   f'составляет {self.fab_consump()}'

    def fab_consump(self):  # расчет расхода ткани
        if self.size == 0:
            if self.height == 0:
                print('Отсутствуют данные о росте и размере')
            else:
                return (2 * float(self.height) + 0.3) * float(self.num_height)
        elif self.height == 0:
            return (float(self.size) / 6.5 + 0.5) * float(self.num_size)
        else:
            return round(
                (2 * float(self.height) + 0.3) * float(self.num_height) + (float(self.size) / 6.5 + 0.5) * float(
                    self.num_size), 2)


class Coat(Clothes):

    def __init__(self, size=0, num_size=0, height=0, num_height=0, year=2022, color = None):
        super().__init__(size, num_size, height, num_height, year)
        self.color = color

    def __str__(self):
        return f'Пальто цвета {self.color} размера {self.size}, ' \
               f'расход ткани на {self.num_size} ед. составляет {self.fab_consump()}'

    def fab_consump(self):
        return round((float(self.size) / 6.5 + 0.5) * float(self.num_size))


class Suit(Clothes):

    def __init__(self, size=0, num_size=0, height=0, num_height=0, year=2022, color = None):
        super().__init__(size, num_size, height, num_height, year)
        self.color = color

    def __str__(self):
        return f'Костюм цвета {self.color}, на рост {self.height}, ' \
               f'расход ткани на {self.num_height} ед. составляет {self.fab_consump()}'

    def fab_consump(self):
        return round((2 * float(self.height) + 0.3) * float(self.num_height))


shirt = Clothes(height=122, num_height=10)
print(shirt)

clothes = Clothes(height=146, num_height=10, size=44, num_size=5, year=2021)
print(clothes)
clothes.year = 2009
print(clothes.year)

coat1 = Coat(size=52, num_size=100, color='red')
print(coat1)

suit1 = Suit(height=188, num_height=200, color='Black')
print(suit1)

#3
class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num - other.num > 0:
            return Cell(self.num - other.num)
        else:
            return 'Количество ячеек в клетке не может быть отрицательным'

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num//other.num)

    def __str__(self):
        return f'Клетка из {self.num} ячеек'

    def make_order(self, lenth):
        a = lenth
        b = self.num//lenth
        c = self.num%lenth
        return 'Клетка: \n' + ('*' * a + '\n') * b + '*' * c

cell1 = Cell(100)
cell2 = Cell(5)

print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1/cell2)
print(cell1.make_order(30))


