import math
while True:
    print('Value A')
    value_a=float(input())
    print('Value B')
    value_b=float(input())
    print('Enter an operation +,-,*,/,^,√')
    operation=str(input())
    if operation=='+':
        result_c=value_a+value_b
        print(result_c)
    if operation=='-':
        result_c=value_a-value_b
        print(result_c)
    if operation=='*':
        result_c=value_a*value_b
        print(result_c)
    if operation=='/':
        result_c=value_a/value_b
        print(result_c)
    if operation=='^':
        result_c=value_a*value_a
        result_d=value_b*value_b
        print('A^2='+str(result_c), 'B^2='+str(result_d))
    if operation=='√':
        result_c=math.sqrt(value_a)
        result_d=math.sqrt(value_b)
        print('√A='+str(result_c), '√B='+str(result_d))
