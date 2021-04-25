user_string = input('Input your string: ')
string_list = user_string.split()
for count in range(len(string_list)):
print(f'{count+1}. {string_list[count][:10]}')