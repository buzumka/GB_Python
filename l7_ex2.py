"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    all_consum = 0  # Переменная для определения общего расхода ткани

    def __init__(self, name, param):
        self.name = name
        self.param = param
        Clothes.all_consum += self.consumption

    @property
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    @property
    def consumption(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):
    @property
    def consumption(self):
        return 2 * self.param + 0.3


suit_one = Suit('Костюм 1', 42)
suit_two = Suit('Костюм 2', 48)
coat_one = Coat('Пальто 1', 155)
coat_two = Coat('Пальто 2', 160)

print(f'Расход ткани всего: {coat_two.all_consum}')
