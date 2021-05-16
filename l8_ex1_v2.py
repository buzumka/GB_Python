"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, data_string, dd=0, mm=0, yyyy=0):
        self.data_string = data_string
        self.dd = dd
        self.mm = mm
        self.yyyy = yyyy

    @classmethod
    def get_dd_mm_yyyy(cls, data_string):
        try:
            dd_l, mm_l, yyyy_l = map(int, data_string.split('-'))
            if cls.validate_data(dd_l, mm_l, yyyy_l) != 0:
                return cls(data_string, dd_l, mm_l, yyyy_l)
        except ValueError:
            print("Дата вводится числами")

    @staticmethod
    def validate_data(day, month, year):
        ind_loc = 1
        if len(str(year)) != 4:
            ind_loc = 0
        if 1 <= month <= 12:
            if (month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31) or (month in [4, 6, 9, 11] and 1 <= day <= 30) or (1 <= day <= 28):
                ind_loc = 1
            else:
                ind_loc = 0
        else:
            ind_loc = 0
        return ind_loc


user_string = input('Введите дату в формате dd-mm-yyyy: ')
try:
    print(f'YYYY: {Data.get_dd_mm_yyyy(user_string).yyyy}, mm: {Data.get_dd_mm_yyyy(user_string).mm}, '
          f'dd: {Data.get_dd_mm_yyyy(user_string).dd}')
except Exception:
    print('Ошибка ввода даты')
