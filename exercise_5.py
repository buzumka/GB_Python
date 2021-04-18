proceeds = float(input('Введите выручку: '))
costs = float(input('Введите издержки: '))
if proceeds > costs:
    result = 'прибыль'
else:
    result = 'убыток'
print(f"У Вас {result}")
if result == 'прибыль':
    print(f"Рентабельность выручки: {(proceeds - costs) / proceeds}")
    num_workers = int(input('Введите количество сотрудников: '))
    profit_worker = (proceeds - costs) / num_workers
    print(f"Прибыль на сотрудника: {profit_worker}")