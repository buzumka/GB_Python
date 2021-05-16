"""
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""


class OfficeEquipments():
    count_in_stor = 0
    dict_control = {}
    count_eq = 0

    def __init__(self, name, price, place, quantity):
        self.name = name
        self.price = price
        self.place = place
        self.quantity = quantity
        OfficeEquipments.count_eq += self.quantity
        self.dict_control['equipments'] = OfficeEquipments.count_eq
        if self.place == 'storage':
            OfficeEquipments.count_in_stor += quantity
            print(f'Оборудование {self.name} принято на склад в количестве {self.quantity} шт.')

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

    @classmethod
    def get_equipments(cls, name, price, place, quantity, arg_one,  arg_two,  arg_three,  arg_four):
        """ Организуем валидацию и создание экземпляра класса"""
        if cls.validate_data(price, quantity, arg_four) == 0:
            return cls(name, price, place, quantity, arg_one,  arg_two,  arg_three,  arg_four)
        else:
            print(f'Ошибка ввода данных для {name}')

    @staticmethod
    def validate_data(price_in, quantity_in, log_param):
        """ Организуем валидацию для целых параметров"""
        ind_loc = 0
        if (type(price_in) != int and type(price_in) != float) or price_in <= 0:
            ind_loc = 1
            print('Ошибка ввода цены | ', end=' ')
        if type(quantity_in) != int or quantity_in <= 0:
            ind_loc = 1
            print('Ошибка ввода количества | ', end=' ')
        if type(log_param) != bool:
            ind_loc = 1
            print('Ошибка ввода логического параметра | ', end=' ')
        return ind_loc


class Printer(OfficeEquipments):
    count_pr = 0
    class_name = 'printers'

    def __init__(self, name, price, place, quantity, list_size, color_param, kind, auto_in):
        OfficeEquipments.__init__(self, name, price, place, quantity)
        self.list_size = list_size
        self.color_param = color_param
        self.kind = kind
        self.auto_in = auto_in
        Printer.count_pr += quantity
        self.dict_control[self.class_name] = Printer.count_pr


class Scanner(OfficeEquipments):
    count_sc = 0
    class_name = 'scanners'

    def __init__(self, name, price, place, quantity, list_size, kind, format_out, auto_in):
        OfficeEquipments.__init__(self, name, price, place, quantity)
        self.list_size = list_size
        self.kind = kind
        self.auto_in = auto_in
        self.format_out = format_out
        Scanner.count_sc += quantity
        self.dict_control[self.class_name] = Scanner.count_sc


class Xerox(OfficeEquipments):
    count_x = 0
    class_name = 'copy machines'

    def __init__(self, name, price, place, quantity, list_size, color_param, kind, auto_in):
        OfficeEquipments.__init__(self, name, price, place, quantity)
        self.list_size = list_size
        self.color_param = color_param
        self.kind = kind
        self.auto_in = auto_in
        Xerox.count_x += self.quantity
        self.dict_control[self.class_name] = Xerox.count_x


"""Создаем экземпляр класса Xerox"""
xerox_one = Xerox.get_equipments("Xerox 530", 2400.00, 'storage', 1, "A4", "color", 'laser', True)

"""Создаем экземпляр класса Scanner"""
scanner_one = Scanner.get_equipments("Epson P-30", '3600', 'storage', 1, 'A4', 'flatbed', 'tiff', "True")

"""Создаем экземпляр класса Printer"""
printer_one = Printer.get_equipments('Xerox 5300', 1400, 'storage', 6, "A3", 'black-white', 'laser', False)
printer_one.get_in_department('Department of Computer Science')
print(printer_one.count_in_stor, printer_one.place)
printer_one.get_in_storage()
print(printer_one.count_in_stor, printer_one.place)
print(printer_one.dict_control)
