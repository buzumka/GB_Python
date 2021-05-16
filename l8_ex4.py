"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class OfficeEquipments:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Printer(OfficeEquipments):
    def __init__(self, name, price, list_size, color_param, kind):
        OfficeEquipments.__init__(self, name, price)
        self.list_size = list_size
        self.color_param = color_param
        self.kind = kind


class Scanner(OfficeEquipments):
    def __init__(self, name, price, list_size, kind):
        OfficeEquipments.__init__(self, name, price)
        self.list_size = list_size
        self.kind = kind


class Xerox(OfficeEquipments):
    def __init__(self, name, price, list_size, color_param, kind, auto_in):
        OfficeEquipments.__init__(self, name, price)
        self.list_size = list_size
        self.color_param = color_param
        self.kind = kind
        self.auto_in = auto_in


xerox_one = Xerox("Xerox 530", 2400, "A4", "color", 'laser', True)
print(xerox_one.kind, ', ', xerox_one.auto_in)