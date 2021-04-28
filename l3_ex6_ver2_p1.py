"""
Задача 6 (версия реализации 2, через собственный модуль)
Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
"""


from l3_ex6_ver2_mod import int_func, check_lat


user_string_in = input("Введите слово (маленькие латинские буквы): ")
if check_lat(user_string_in) == 1:
    print("Введеная строка не удовлетворяет параметрам")
else:
    print(int_func(user_string_in))
