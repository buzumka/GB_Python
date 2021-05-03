"""
6. Сформировать (не программно) текстовый файл.
В нём каждая строка должна описывать учебный предмет и наличие лек-ых, практ-их и лаб-ых занятий по предмету.
Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести его на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def sum_hours(string_hours):
    list_loc = string_hours.split()
    sum_loc = 0
    for el_l in list_loc:
        list_split = el_l.split('(')
        if list_split[0].isdigit():
            sum_loc += int(list_split[0])
    return sum_loc


""" Обработка входящего файла"""
file_name = "lessons_in.txt"
list_lesson = []
list_h = []
with open(file_name) as f_obj:
    for line in f_obj:
        list_mid = line.split(':')
        list_lesson.append(list_mid[0])
        list_h.append(list_mid[1])

""" Суммируем и делаем словарь """
dict_out = {}
for n in range(len(list_lesson)):
    dict_out[list_lesson[n]] = sum_hours(list_h[n])

print(f'Словарь - {dict_out}')
