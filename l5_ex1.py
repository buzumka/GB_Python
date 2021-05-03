"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

from f_works_mod import f_create

""" Формируем содержимое файла """
user_string = input("Введите строку (окончание ввода - пустая строка): ")
list_strings = []
while user_string != '':
    user_string += '\n'
    list_strings.append(user_string)
    user_string = input("Введите строку (окончание ввода - пустая строка): ")

""" Создаем и записываем файл """
f_create("out_file.txt", list_strings)