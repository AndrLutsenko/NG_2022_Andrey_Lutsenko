import datetime 
print('Number of seconds')
sec=int(input()) 
format_time = str(datetime.timedelta(seconds = sec)) 
print("Converted time: ",format_time)
