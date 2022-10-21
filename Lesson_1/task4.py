import math
print('Value a')
value_a=int(input()) 
print('Value b')
value_b=int(input()) 
print('Value c')
value_c=int(input()) 
discriminant=value_b*value_b-(4*value_a*value_c)
print('Discriminant= ',discriminant)
if discriminant>0:
    x1=(-value_b+math.sqrt(discriminant))/(2*value_a)
    x2=(-value_b-math.sqrt(discriminant))/(2*vale_a)
    print(f'x1={x1} x2={x2}')
if discriminant==0:
    x0=(-value_b)/(2*value_a)
    print(f'x={x0}')
if discriminant<0:
    print(f'There are no roots')
