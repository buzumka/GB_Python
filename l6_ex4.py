"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    is_police = False

    def __init__(self, speed_in, color_in, name_in):
        self.speed = speed_in
        self.color = color_in
        self.name = name_in

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость машины {self.name}  - {self.speed}')


class TownCar(Car):
    car_class = 'городской'
    is_police = False

    def show_speed(self):
        if self.speed > 60: print(f'Превышение скорости')

class WorkCar(Car):
    car_class = 'рабочий'
    is_police = False


    def show_speed(self):
        if self.speed > 40: print(f'Превышение скорости')

class SportCar(Car):
    car_class = 'спортивный'
    is_police = False

class PoliceCar(Car):
    car_class = 'полицейский'
    is_police = True


police_car_one = PoliceCar(60,'бело-синий', 'Полицейский рено №1')
print(f'Машина класса {police_car_one.car_class} (полицейская - {police_car_one.is_police}), цвет {police_car_one.color}')
police_car_one.show_speed()
police_car_one.go()
police_car_one.turn("направо")
police_car_one.stop()

print('')
town_car_one = TownCar(70,'синий', 'Тайота Рав4')
print(f'Машина класса {town_car_one.car_class} (полицейская - {town_car_one.is_police}), цвет {town_car_one.color}')
town_car_one.go()
town_car_one.show_speed()
town_car_one.turn("направо")
town_car_one.stop()

print('')
work_car_one = WorkCar(50,'красный', 'Тайота Tundra')
print(f'Машина класса {work_car_one.car_class} (полицейская - {work_car_one.is_police}), цвет {work_car_one.color}')
work_car_one.go()
work_car_one.show_speed()
work_car_one.turn("направо")
work_car_one.stop()

print('')
sport_car_one = SportCar(160,'белый', 'Mustang')
print(f'Машина класса {sport_car_one.car_class} (полицейская - {sport_car_one.is_police}), цвет {sport_car_one.color}')
sport_car_one.show_speed()
sport_car_one.go()
sport_car_one.turn("направо")
sport_car_one.stop()
