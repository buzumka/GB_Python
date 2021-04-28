"""
итератор, повторяющий элементы некоторого списка, определенного заранее
"""

from itertools import cycle

n = 0
list_in = ['Вадик', 'Дима', 'Леонид', 'Татьяна']
for el in cycle(list_in):
    if n > 10:
        break
    else:
        print(el)
        n += 1
