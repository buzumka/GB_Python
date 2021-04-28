"""
(версия реализации 2, через собственный модуль)
Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


from l3_ex6_ver2_mod import int_func, check_lat

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