dicts=input(dict())#"Enter the string: ")
print(f'Your string: ', dicts)
#Exercise 1
s_string = set(dicts)
print(s_string)
s_string = set(dicts) #non-repeating elements
summ = [] #Summation of elements
#Exercise 2
for s_symbol in s_string:
    count = 0
    for symbol in dicts:
        if s_symbol == symbol:
            count += 1
    summ.append(f'{s_symbol}= {count}')
    summ.sort()
for item in summ:
    print(item)