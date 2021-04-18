day_result = int(input('Введите пробег в первый день: '))
desired_result = int(input('Введите желаемый пробег: '))
count = 1
while day_result < desired_result:
    day_result *= 1.1
    count += 1
print(f"На {count}-ой день спортсмен достиг результата - не менее {desired_result} км")