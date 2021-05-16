"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию.
"""


class OwnDevisionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


dividend_in = input("Введите делимое: ")
divider_in = input("Введите делитель: ")

try:
    dividend_in = int(dividend_in)
    divider_in = int(divider_in)
    if divider_in == 0:
        raise OwnDevisionByZero("Делить на ноль нельзя!")
except ValueError:
    print("Должны быть введены числа")
except OwnDevisionByZero as err:
    print(err)
else:
    print(f"Результат деления числа {dividend_in} на число {divider_in}: {dividend_in/divider_in}")
