# 1
import time
import keyboard
import threading

class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        print('Для выключения светофора нажмите "q"')
        def running_1():
            while True:
                print(self.__color[0])
                time.sleep(7)
                print(self.__color[1])
                time.sleep(2)
                print(self.__color[2])
                time.sleep(8)
        run = threading.Thread(target=running_1, daemon=True)
        run.start()
        keyboard.wait(hotkey='q')

tl1 = TrafficLight()
tl1.running()

# 2
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self, weight1m = 1.0, thick = 1.0):
        weight_road = self._length*self._width*weight1m*thick
        kg_ton = 'кг' if weight_road<1000.0 else 'тонн'
        return f'Масса асфальта для покрытия дороги длиной {self._length} м, шириной {self._width} м и толщиной {thick} см составляет {round(weight_road, 2) if weight_road<1000.0 else round(weight_road/1000, 2)} {kg_ton}'

road1 = Road(float(input('Введите длину дорожного покрытия: ')), float(input('Введите ширину дорожного покрытия: ')))
print(road1.weight(25, float(input('Введите толщину дорожного покрытия: '))))

#3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': float(wage), 'bonus': float(bonus)}

class Position(Worker):
    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

position1 = Position('Anna', 'Petrova', 'manager', 10000.1, 5000.2)
print(f'Имя: {position1.name}')
print(f'Фамилия: {position1.surname}')
print(f'Оклад и бонус: {position1._income}')

full_name = position1.get_full_name()
total_income = position1.get_total_income()
print(f'Имя и фамилия: {full_name}')
print(f'Доход: {total_income}')

#4
class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn(self, direction):
        print(f'Машина повернула {direction}')
    def show_speed(self):
        print(f'Текущая скорость {self.speed}')

class TownCar(Car):
    def car_type(self):
        print('Городская машина')

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')
        if self.speed>60:
            print('Вы превышаете допустимую скорость!!!')

class SportCar(Car):
    def car_type(self):
        print('Спортивная машина')
    def __init__(self, speed, max_speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.max_speed = max_speed

    def max_speed_info(self):
        print(f'Спортивная машина может разгоняться до {self.max_speed} км/ч')

class WorkCar(Car):
    def car_type(self):
        print('Рабочая машина')
    def show_speed(self):
        print(f'Текущая скорость {self.speed}')
        if self.speed>40:
            print('Вы превышаете допустимую скорость!!!')

class PoliceCar(Car):
    def car_type(self):
        print('Служебная машина')
    def __init__(self, speed, color, name, is_police = True):
        super().__init__(speed, color, name)
        self.is_police = is_police
    def police_info_speed(self):
        print('Полицейские машины могут превышать допустимую скорость при включенных проблесковых маячках и звуковом сигнале')

town_car1 = TownCar(100, 'red', 'Toyota')
town_car1.car_type()
print(town_car1.color)
print(town_car1.speed)
print(town_car1.name)
print('Полицейская машина' if town_car1.is_police else 'Не является полицейской машиной')
town_car1.go()
town_car1.stop()
town_car1.turn('вправо')
town_car1.show_speed()
print(' ')

sport_car1 = SportCar(100, 300, 'black', 'Ferrari')
sport_car1.car_type()
print(sport_car1.color)
print(sport_car1.speed)
print(sport_car1.name)
print('Полицейская машина' if sport_car1.is_police else 'Не является полицейской машиной')
sport_car1.go()
sport_car1.stop()
sport_car1.turn('влево')
sport_car1.show_speed()
sport_car1.max_speed_info()
print(' ')

work_car1 = WorkCar(30, 'white', 'Gazel')
work_car1.car_type()
print(work_car1.color)
print(work_car1.speed)
print(work_car1.name)
print('Полицейская машина' if work_car1.is_police else 'Не является полицейской машиной')
work_car1.go()
work_car1.stop()
work_car1.turn('вправо')
work_car1.show_speed()
print(' ')

police_car1 = PoliceCar(100, 'white and blue', 'Ford')
police_car1.car_type()
print(police_car1.color)
print(police_car1.speed)
print(police_car1.name)
print('Полицейская машина' if police_car1.is_police else 'Не является полицейской машиной')
police_car1.go()
police_car1.stop()
police_car1.turn('вправо')
police_car1.show_speed()
police_car1.police_info_speed()

#5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки с использованием ручки {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки с использованием карандаша {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки с использованием маркера {self.title}')

pen1 = Pen('шариковая')
print(pen1.title)
pen1.draw()

pencil1 = Pencil('простой')
print(pencil1.title)
pencil1.draw()

handle1 = Handle('цветной маркер')
print(handle1.title)
handle1.draw()