"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц)
Результатом сложения должна быть новая матрица.
"""


class Matrix:
    """ Описываем класс Matrix, перезагружаем операторы """
    def __init__(self, list_lists):
        self.n_strings = len(list_lists)
        self.m_rows = len(list_lists[0])
        self.matrix = list_lists
        self.string_loc = ''

    def __add__(self, other):
        return Matrix(
            [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.m_rows)] for i in range(self.n_strings)]
            )

    def __str__(self):
        return '\n'.join(' '.join(str(self.matrix[i_str][j_row]) for j_row in range(self.m_rows))
                         for i_str in range(self.n_strings))


my_mat_a = Matrix([[1, 2], [1, 2], [1, 2]])
my_mat_b = Matrix([[-1, 2], [2, 2], [0, 2]])
my_mat_c = Matrix([[-1, 0], [2, 1], [0, -2]])

print('Матрица А')
print(my_mat_a)
print('Матрица В')
print(my_mat_b)
print('Матрица D = А + В + C')
print(my_mat_a + my_mat_b + my_mat_c)
