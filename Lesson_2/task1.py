#String input
print('Enter the string: ')
string=input()
print(f'Your string: ',str(string))
#Exercise 1
s_string = set(string) #non-repeating elements
summ = [] #Summation of elements
#Exercise 2
for s_symbol in s_string:
    count = 0
    for symbol in string:
        if s_symbol == symbol:
            count += 1
    summ.append(f'{s_symbol}= {count}')
    summ.sort()
for item in summ:
    print(item)