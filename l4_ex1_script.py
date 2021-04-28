"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, work_hours, rate, prize = argv
work_hours_fl = float(work_hours)
rate_fl = float(rate)
prize_fl = float(prize)
print(f"Расчет заработной платы: {work_hours_fl * rate_fl +  prize_fl}")
