"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title_in):
        self.title = title_in

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')


stationery_one = Stationery("Синяя скрепка")
print(stationery_one.title)
stationery_one.draw()

print(' ')
pen_one = Pen("Синяя ручка")
print(pen_one.title)
pen_one.draw()

print(' ')
pencil_one = Pencil("Синий карандаш")
print(pencil_one.title)
pencil_one.draw()

print(' ')
handle_one = Handle("Синяя ручка")
print(handle_one.title)
handle_one.draw()
