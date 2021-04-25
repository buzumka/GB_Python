"""
Задача 6
Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
"""


def int_func(user_string):
    """ Возвращает слово, переданное аргументом user_string, написанным с заглавной буквы"""
    return user_string.title()


def check_lat(user_string):
    """ Принимает на вход строку и выдает на выход 1, если не все буквы маленькие латинские"""
    for letter in user_string:
        if (ord(letter) < 97) or (ord(letter) > 122):
            return 1


user_string_in = input("Введите слово (маленькие латинские буквы): ")
if check_lat(user_string_in) == 1:
    print("Введеная строка не удовлетворяет параметрам")
else:
    print(int_func(user_string_in))
