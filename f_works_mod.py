""" Создаем файл"""


def f_create (file_name, user_list):
    with open(file_name, "w") as f_obj:
        f_obj.writelines(user_list)
    print(f'Создан файл {file_name}')