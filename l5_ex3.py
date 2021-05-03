"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""


def avg(list_f):
    """ Возвращает среднее списка """
    s_loc = 0
    for el in list_f:
        s_loc += el
    return s_loc / len(list_f)


file_name = "f_workers.txt"
list_workers = []
list_salaries = []
try:
    """ Обработка файла """
    with open(file_name) as f_obj:
        for line in f_obj:
            list_mid = line.split()
            list_workers.append(list_mid[0])
            list_salaries.append(float(list_mid[1]))
    """ Печатаем сотрудников с зарплатой менее 20000"""
    print('Сотрудники с зарплатой менее 20000:')
    for index in range(len(list_salaries)):
        if list_salaries[index] <= 20000:
            print(list_workers[index])
    print(f'Средняя зарплата сотрудников: {avg(list_salaries)}')
except FileNotFoundError:
    print('Файл не найден')
