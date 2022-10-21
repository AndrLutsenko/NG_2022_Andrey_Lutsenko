print('Number of seconds')
seconds=int(input()) 
second=seconds
minute=second/60
hour=minute/60
days=hour/24
print(f'Days={int(days)}', f'Hour={int(hour%24)}', f'Minute={int(minute%60)}', f'Second={int(second%60)}')
