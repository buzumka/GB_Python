"""
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
Дополнительно реализован подсчет слов в файле
"""


def count_word(string_list):
    list_loc = string_list[0:-2].split()
    return len(list_loc)


file_name = "in_file.txt"
list_in = []
with open(file_name) as f_obj:
    for line in f_obj:
        list_in.append(line)

print(f'Количество строк в файле {file_name} - {len(list_in)}')
n = 1
count_f_word = 0
for string in list_in:
    print(f'Количество слов в {n}-ой строке: {count_word(string)}')
    count_f_word += count_word(string)
    n += 1
print(f'Количество слов в в файле {file_name} - {count_f_word}')
