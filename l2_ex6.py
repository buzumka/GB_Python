list_products = []
len_list_product = int(input('Input number of products: '))
list_product_characteristics = ["name", 'price', 'quantity', 'unit']

# create list of products
for count in range(len_list_product):
    list_middle = []
    list_value = []
    # input values
    for count_val in range(len(list_product_characteristics)):
        value_name = input(f'Input product {list_product_characteristics[count_val]}: ')
        if value_name.isdigit():
            value_name = int(value_name)
        list_value.append(value_name)
    dict_product = {list_product_characteristics[a]: list_value[a] for a in range(len(list_product_characteristics))}
    list_middle.append(count+1)
    list_middle.append(dict_product)
    list_products.append(tuple(list_middle))
print(list_products)

# analytics
list_analitics = []
for count_val in range(len(list_product_characteristics)):
    list_value = []
    for count in range(len_list_product):
        list_middle = []
        list_middle = list(list_products[count])
        list_value.append(list_middle[1].get(list_product_characteristics[count_val]))
    list_analitics.append(list_value)
dict_analitics = {list_product_characteristics[i]: list_analitics[i] for i in range(len(list_product_characteristics))}
print(dict_analitics)