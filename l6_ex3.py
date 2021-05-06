"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name_in, surname_in, w_position_in, wage, bonus):
        self.name = name_in
        self.surname = surname_in
        self.w_position = w_position_in
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return ' '.join([self.name, self.surname])


    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])


position_ii_january = Position('Иван', 'Иванов', 'программист', 125000, 20000)
print(f'Доход {position_ii_january.get_full_name()} за январь: ')
position_ii_january.get_total_income()

position_pp_january = Position('Петр', 'Петров', 'бухгалтер', 75000, 25000)
print(f'Доход {position_pp_january.get_full_name()} за январь: ')
position_pp_january.get_total_income()

position_td_january = Position('Татьяна', 'Дорохова', 'директор', 250000, 70000)
print(f'Доход {position_td_january.get_full_name()} за январь: ')
position_td_january.get_total_income()
