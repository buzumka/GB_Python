"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
Реализую для целых чисел - для рациональных все то же самое
"""

from f_works_mod import f_create
""" Формируем содержимое файла """

user_string = input("Введите целое число (окончание ввода - пустая строка): ")
list_strings = []
while user_string != '':
    if user_string.isdigit():
        user_string += ' '
        list_strings.append(user_string)
        user_string = input("Введите целое число (окончание ввода - пустая строка): ")
    else:
        user_string = input("Ошибка ввода. Введите целое число (окончание ввода - пустая строка): ")

""" Создаем и записываем файл """
f_create("out_file_num.txt", list_strings)

"""" Считаем сумму """
file_name_s = "out_file_num.txt"
string_num = ''
with open(file_name_s) as f_obj:
    for line in f_obj:
        string_num = line
list_string = string_num.split()
sum_my = 0
for el in list_string:
    sum_my += int(el)
print(f'Сумма чисел в строке файла {file_name_s} = {sum_my}')
