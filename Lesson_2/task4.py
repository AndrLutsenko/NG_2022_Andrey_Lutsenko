print('Enter factorial values: ')
factorial_value=int(input())
fv=factorial_value #For a clear derivation of the factorial
factorial=1
while factorial_value>=1:
    factorial*=factorial_value
    factorial_value-=1
print(f'{fv}!= {factorial}')