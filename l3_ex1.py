"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def devided(dividend, divider):
    """Реализует деление dividend на divider с обработкой деления на ноль"""
    try:
        return dividend / divider
    except ZeroDivisionError:
        return


user_dividend = float(input("Делимое: "))
user_divider = float(input("Делитель: "))
print(f'Частное = {devided(user_dividend, user_divider)}')
