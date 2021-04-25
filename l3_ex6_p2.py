"""
Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(user_string):
    """ Возвращает слово, переданное аргументом user_string, написанным с заглавной буквы"""
    return user_string.title()


def check_lat(user_string):
    """ Принимает на вход строку и выдает на выход 1, если не все буквы маленькие латинские"""
    for letter in user_string:
        if (ord(letter) < 97) or (ord(letter) > 122):
            return 1


user_string_in = input("Введите строку из слов, разделенных пробелом (маленькие латинские буквы): ")
list_user_string = user_string_in.split()  # Разделяем строки по пробелу
string_ex = ""
switch = 0
for string in list_user_string:  # Цикл проверки на соотвествие ввода
    if check_lat(string) == 1:
        switch = 1
        print("Введеная строка не удовлетворяет параметрам")
        break
    else:
        string_ex += int_func(string) + " "
if switch != 1: print(string_ex)
