user_month = int(input('Input number of month: '))
month_dict = {'Winter': [12, 1, 2], 'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Fall': [9, 10, 11]}
for key in month_dict:
    if user_month in month_dict.get(key):
        print(key)