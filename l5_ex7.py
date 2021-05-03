"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.

Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

import json

""" Читаем файл"""
file_name = "firms_in.txt"
list_f_name = []
list_f_form = []
list_f_inc = []
list_f_prod_cost = []
with open(file_name) as f_obj:
    for line in f_obj:
        list_mid = line.split()
        list_f_name.append(list_mid[0])
        list_f_form.append(list_mid[1])
        list_f_inc.append(int(list_mid[2]))
        list_f_prod_cost.append(int(list_mid[3]))

""" Среднее значение прибыли и попутно словарь прибыли"""
n = 0  # Счетчик
sum_avg = 0
dict_profit = {}
for i in range(len(list_f_inc)):
    dict_profit[list_f_name[i]] = list_f_inc[i] - list_f_prod_cost[i]
    if (dict_profit[list_f_name[i]]) > 0:
        sum_avg += dict_profit[list_f_name[i]]
        n += 1
try:
    avg_profit = sum_avg / n
    print(f'Средняя прибыль: {avg_profit}')
except ZeroDivisionError:
    print('Прибыль всех фирм отрицательна')
    avg_profit = 'Нет прибыли'

""" Выходной список"""
dict_avg = {}
dict_avg["average_profit"] = avg_profit
list_out = [dict_profit, dict_avg]
print(f'Выходной список: {list_out}')

""" Пишем json файл"""
j_file = "my_file_json.json"
with open(j_file, "w") as write_f:
    json.dump(list_out, write_f)
print(f"JSON файл {j_file} записан")
