import math

class Passport():
    def __init__(self, first_name, last_name, country, date_of_birth, numb_of_pasport):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.country = country
        self.numb_of_pasport = numb_of_pasport

    def PrintInfo(self):
        print("\nFullname: ", self.first_name, " ", self.last_name)
        print("Date of birth: ", self.date_of_birth)
        print("Country: ", self.country)
        print("Passport number: ", self.numb_of_pasport)

class ForeignPassport(Passport):
    def __init__(self, first_name, last_name, country, date_of_birth, numb_of_pasport, visa):
        super().__init__(first_name, last_name, country, date_of_birth, numb_of_pasport)
        self.visa = visa

    def PrintInfo(self):
        super().PrintInfo()
        print("Visa: ", self.visa)

PassportList = []
request = ForeignPassport('Ivan', 'Ivanov', 'Russia', '12.03.1967', '123456789', 'USA')
PassportList.append(request)
request = Passport('Иван', 'Иванов', 'Россия', '12.03.1967', '45001432')
PassportList.append(request)
request = ForeignPassport('Peter', 'Smit', 'USA', '01.03.1990', '21435688', 'Germany')
PassportList.append(request)

for emp in PassportList:
    emp.PrintInfo()



class Equipment:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year

    def action(self):
        return 'Не определено'

    def __str__(self):
        return f'{self.name} {self.make} {self.year}'

class Printer(Equipment):
    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series

    def __str__(self):
        return f'{self.name} {self.series} {self.make} {self.year}'

    def action(self):
        return 'Печатает'

class Scaner(Equipment):
    def action(self):
        return 'Сканирует'

class Xerox(Equipment):
    def action(self):
        return 'Копирует'

sklad = []

scaner = Scaner('Mustek', 'BearPow 1200CU', 2010)
sklad.append(scaner)

xerox = Xerox('Xerox', 'Phaser 3120', 2019)
sklad.append(xerox)

printer = Printer("1200", 'hp', 'Laser Jet', 2018)
sklad.append(printer)

print("На складе имеются:")

for x in sklad:
    print(x, end=' ')
    print(x.action())

sklad = [x for x in sklad if not isinstance(x, Printer)]

print("\nНа складе осталось:")

for x in sklad:
    print(x, end=' ')
    print(x.action())










from random import randint

class Soldier:
    def __init__(self, name='Noname', health=100):
        self.name = name
        self.health = health

    def set_name(self, name):
        self.name = name

    def make_kick(self, enemy):
        enemy.health -= 20
        if enemy.health < 0:
            enemy.health = 0
        self.health += 10
        print(self.name, "бьет", enemy.name)
        print('%s = %d' % (enemy.name, enemy.health))

class Battle:
    def __init__(self, u1, u2):
        self.u1 = u1
        self.u2 = u2
        self.result = ''

    def battle(self):
        while self.u1.health > 0 and self.u2.health > 0:
            n = randint(1, 2)
            if n == 1:
                self.u1.make_kick(self.u2)
            else:
                self.u2.make_kick(self.u1)
        if self.u1.health > self.u2.health:
            self.result = self.u1.name + " ПОБЕДИЛ"
        elif self.u2.health > self.u1.health:
            self.result = self.u2.name + " ПОБЕДИЛ"

    def who_win(self):
        print(self.result)

first = Soldier('Mr. First', 140)
second = Soldier()
second.set_name('Mr. Second')
b = Battle(first, second)
b.battle()
b.who_win()










import random

class Card:
    NumsList = ["Джокер", '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
    MastList = ["пик", "крестей", "бубей", "червей"]

    def __init__(self, i, j):
        self.Mastb = self.MastList[i - 1]
        self.Num = self.NumsList[j - 1]

class DeckOfCards:
    def __init__(self):
        self.deck = [None] * 56
        k = 0
        for i in range(1, 4 + 1):
            for j in range(1, 14 + 1):
                self.deck[k] = Card(i, j)
                k += 1

    def shuffle(self):
        random.shuffle(self.deck)

    def get(self, i):
        if 0 <= i <= 55:
            answer = self.deck[i].Num
            answer += " "
            answer += self.deck[i].Mastb
        else:
            answer = "В колоде только 56 карт"
        return answer

deck = DeckOfCards()
deck.shuffle()
print('Выберите карту из колоды из 56 карт:')
n = int(input())
if 0 < n <= 56:
    card = deck.get(n - 1)
    print('Вы взяли карту:', card)
else:
    print("В колоде только 56 карт")






class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def display(self):
        print(f"({self.x}, {self.y}, {self.z})")

    def read(self):
        self.x = float(input("Введите x: "))
        self.y = float(input("Введите y: "))
        self.z = float(input("Введите z: "))

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Vector3D):
            # Скалярное произведение
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            # Умножение на скаляр
            return Vector3D(self.x * other, self.y * other, self.z * other)

    def __matmul__(self, other):
        # Векторное произведение
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector3D(x, y, z)

# Пример использования
v1 = Vector3D(4, 1, 2)
v1.display()

v2 = Vector3D()
v2.read()

v3 = Vector3D(1, 2, 3)

v4 = v1 + v2
v4.display()

a = v4 * v3
print(a)

v4 = v1 * 10
v4.display()

v4 = v1 @ v3
v4.display()
















class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def increase_side(self, percentage):
        self.base *= (1 + percentage / 100)
        self.height *= (1 + percentage / 100)

    def decrease_side(self, percentage):
        self.base *= (1 - percentage / 100)
        self.height *= (1 - percentage / 100)

    def calculate_circumcircle_radius(self):
        hypotenuse = math.sqrt(self.base ** 2 + self.height ** 2)
        return hypotenuse / 2

    def calculate_perimeter(self):
        hypotenuse = math.sqrt(self.base ** 2 + self.height ** 2)
        return self.base + self.height + hypotenuse

    def calculate_angles(self):
        alpha = math.degrees(math.atan(self.height / self.base))
        beta = 90 - alpha
        return 90, alpha, beta

triangle = RightTriangle(3, 4)
print("База: ", triangle.base)
print("высота:", triangle.height)

triangle.increase_side(10)
print("Увеличенные борта:")
print("база:", triangle.base)
print("высота:", triangle.height)

circumcircle_radius = triangle.calculate_circumcircle_radius()
print("Радиус окружности:", circumcircle_radius)

perimeter = triangle.calculate_perimeter()
print("Периметр:", perimeter)

angles = triangle.calculate_angles()
print("Углы (градусы):")
print("90 градусов (прямой угол)")
print("Альфа:", angles[1])
print("Бета:", angles[2])





class Bus:
    def __init__(self, max_speed, capacity):
        self.speed = 0
        self.capacity = capacity
        self.max_speed = max_speed
        self.passengers = []
        self.hasEmptySeats = True
        self.seats = {i: None for i in range(1, capacity + 1)}

    def board_passengers(self, passenger_names):
        if not self.hasEmptySeats:
            print("Автобус уже полон.")
            return
        for passenger_name in passenger_names:
            if len(self.passengers) < self.capacity:
                self.passengers.append(passenger_name)
                for seat, occupant in self.seats.items():
                    if occupant is None:
                        self.seats[seat] = passenger_name
                        break
            else:
                print(f"Больше нет свободных мест на {passenger_name}. автобус заполнен.")
        self.update_empty_seats()

    def disembark_passengers(self, passenger_names):
        for passenger_name in passenger_names:
            if passenger_name in self.passengers:
                self.passengers.remove(passenger_name)
                for seat, occupant in self.seats.items():
                    if occupant == passenger_name:
                        self.seats[seat] = None
        self.update_empty_seats()

    def increase_speed(self, value):
        if self.speed + value <= self.max_speed:
            self.speed += value
        else:
            print("Нельзя превышать максимальную скорость.")

    def decrease_speed(self, value):
        if self.speed - value >= 0:
            self.speed -= value
        else:
            print("Скорость не может опускаться ниже 0.")

    def update_empty_seats(self):
        self.hasEmptySeats = len(self.passengers) < self.capacity

    def __contains__(self, passenger_name):
        return passenger_name in self.passengers

    def __iadd__(self, passenger_name):
        self.board_passengers([passenger_name])
        return self

    def __isub__(self, passenger_name):
        self.disembark_passengers([passenger_name])
        return self

bus = Bus(max_speed=60, capacity=50)

bus.board_passengers(["Alice", "Bob", "Charlie"])
bus += "David"

print("Пассажиры:", bus.passengers)
print("сидящие: ", bus.seats)
print("Есть свободные места: ", bus.hasEmptySeats)

bus.disembark_passengers(["Alice"])
bus -= "Bob"

print("Пассажиры:", bus.passengers)
print("сидящие:", bus.seats)
print("Есть свободные места: ", bus.hasEmptySeats)

bus.increase_speed(20)
print("Текущая скорость:", bus.speed)

bus.decrease_speed(10)
print("Текущая скорость:", bus.speed)
