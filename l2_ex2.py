len_list_user = int(input('Input list length: '))
list_user = []
for count in range(len_list_user):
    list_user.append(input('Input element: '))
for count in range(0, (len_list_user//2)*2, 2):
    list_user[count], list_user[count+1] = list_user[count+1], list_user[count]
print(list_user)