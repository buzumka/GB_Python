"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре. 
В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). 
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Необходимо собрать аналитику о товарах. 
Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
"""

list_products = []
list_product_characteristics = ["name", 'price', 'quantity', 'unit']
index = 1
# create list of products
"""
Пример готовой структуры:

[

(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
"""
while True:
    answer = input('Добавить новый товар? (да/нет): ')
    if answer.upper() == "НЕТ":
        break
    else:
        list_middle = []
        dict_product = {}
        # input values
        for spec in list_product_characteristics:
            value_name = input(f'Введите {spec} товара: ')
            if value_name.isdigit():
                dict_product[spec] = int(value_name)
            else:
                dict_product[spec] = value_name
        list_products.append(tuple([index, dict_product]))
        index += 1
print (list_products)

# analytics
"""
Пример:

{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

list_analitics = []
for count_val in range(len(list_product_characteristics)):
    list_value = []
    for count in range(len(list_products)):
        list_middle = []
        list_middle = list(list_products[count])
        list_value.append(list_middle[1].get(list_product_characteristics[count_val]))
    list_analitics.append(list_value)
dict_analitics = {list_product_characteristics[i]: list_analitics [i] for i in range(len(list_product_characteristics))}
print (dict_analitics)