"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

from f_works_mod import f_create

dict_num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

file_name = "f_num_en.txt"
list_strings = []
list_salaries = []
try:
    """ Обработка  входного файла """
    with open(file_name) as f_obj:
        for line in f_obj:
            list_mid = line.split()
            string_mid = dict_num.setdefault(list_mid[0]) + ' ' + list_mid[1] + ' ' + list_mid[2] + '\n'
            list_strings.append(string_mid)
except FileNotFoundError:
    print('Файл не найден')

""" Создаем и записываем файл """
f_create("f_num_en_out.txt", list_strings)