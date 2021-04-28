"""
Задача 6 (версия реализации 2, через собственный модуль)
Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
В модуле реализованы функции: проверки на соотвествие условия ввода и превращения 1й буквы в заглавную
"""


def int_func(user_string):
    """ Возвращает слово, переданное аргументом user_string, написанным с заглавной буквы"""
    return user_string.title()


def check_lat(user_string):
    """ Принимает на вход строку и выдает на выход 1, если не все буквы маленькие латинские"""
    for letter in user_string:
        if (ord(letter) < 97) or (ord(letter) > 122):
            return 1