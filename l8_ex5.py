"""
5. Продолжить работу над первым заданием 4.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
"""


class OfficeEquipments:
    count_in_stor = 0
    dict_control = {}
    count_eq = 0

    def __init__(self, name, price, place='storage'):
        self.name = name
        self.price = price
        self.place = place
        OfficeEquipments.count_eq += 1
        self.dict_control['equipments'] = OfficeEquipments.count_eq
        if self.place == 'storage':
            OfficeEquipments.count_in_stor += 1
            print(f'Оборудование {self.name} принято на склад')

    def get_in_department(self, name_department):
        """ Организуем передачу в подразделение"""
        if self.place == 'storage':
            OfficeEquipments.count_in_stor -= 1
        self.place = name_department

    def get_in_storage(self):
        """Организуем передачу на склад"""
        if self.place != 'storage':
            OfficeEquipments.count_in_stor += 1
        self.place = 'storage'


class Printer(OfficeEquipments):
    count_pr = 0
    class_name = 'printers'

    def __init__(self, name, price, list_size, color_param, kind, place='storage'):
        OfficeEquipments.__init__(self, name, price, place)
        self.list_size = list_size
        self.color_param = color_param
        self.kind = kind
        self.count_pr += 1
        self.dict_control[self.class_name] = self.count_pr


class Scanner(OfficeEquipments):
    count_sc = 0
    class_name = 'scanners'

    def __init__(self, name, price, list_size, kind, place='storage'):
        OfficeEquipments.__init__(self, name, price, place)
        self.list_size = list_size
        self.kind = kind
        self.count_sc += 1
        self.dict_control[self.class_name] = self.count_sc


class Xerox(OfficeEquipments):
    count_x = 0
    class_name = 'copy machines'

    def __init__(self, name, price, list_size, color_param, kind, auto_in, place='storage'):
        OfficeEquipments.__init__(self, name, price, place)
        self.list_size = list_size
        self.color_param = color_param
        self.kind = kind
        self.auto_in = auto_in
        self.count_x += 1
        self.dict_control[self.class_name] = self.count_x


xerox_one = Xerox("Xerox 530", 2400, "A4", "color", 'laser', True)
scanner_one = Scanner("Epson P-30", 3600, "A4", 'flatbed')
printer_one = Printer('Xerox 5300', 1400, "A3", 'black-white', 'laser')
printer_one.get_in_department('Department of Computer Science')

print(xerox_one.dict_control)
print(printer_one.count_in_stor, printer_one.place)
printer_one.get_in_storage()
print(printer_one.count_in_stor, printer_one.place)
