seconds_in = int(input('Enter time in seconds: '))
seconds = seconds_in%60
minutes_in = seconds_in//60
minutes = minutes_in%60
hours_in = minutes_in//60
hours = hours_in%60
print (f'Time: {hours}.{minutes}.{seconds}')