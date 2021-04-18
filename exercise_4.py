number = int(input('Введите целое число: '))
digits_list = []
count = 0
number_slice = number
while number >= 10**(count):
    digits_list.append(number_slice%10)
    number_slice //= 10
    count += 1
print(f"Максимальная цифра числа {number}: {max(digits_list)}")