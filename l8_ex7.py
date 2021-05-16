"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class Complex:
    """ Описываем класс Complex, перезагружаем операторы """
    def __init__(self, part_re, part_im):
        self.part_re = part_re
        self.part_im = part_im

    def __add__(self, other):
        return Complex(self.part_re + other.part_re, self.part_im + other.part_im)

    def __mul__(self, other):
        """ (re1re2−im1im2)+(re1im2+im1re2)i"""
        return Complex(self.part_re * other.part_re - self.part_im * other.part_im,
                       self.part_re * other.part_im + self.part_im * other.part_re)

    def __str__(self):
        if self.part_im > 0:
            return str(self.part_re) + " + " + str(self.part_im) + ' * i'
        elif self.part_im < 0:
            return str(self.part_re) + " - " + str(abs(self.part_im)) + ' * i'
        else:
            return str(self.part_re)


my_z_one = Complex(-1, 2)
my_z_two = Complex(2, -2)
my_z_three = Complex(-1, 0)

print(f'Комплексное число z1 = {my_z_one}')
print(f'Комплексное число z2 = {my_z_two}')
print(f'Комплексное число z3 = {my_z_three}')
print(f'z3 + z3 * z1 = {my_z_three + my_z_two * my_z_one}')