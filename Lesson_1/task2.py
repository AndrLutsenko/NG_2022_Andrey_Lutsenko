import math
while True:
    print('Value A')
    a=float(input())
    print('Value B')
    b=float(input())
    print('Enter an operation +,-,*,/,^,√')
    operation=str(input())
    if operation=='+':
        c=a+b
        print(c)
    if operation=='-':
        c=a-b
        print(c)
    if operation=='*':
        c=a*b
        print(c)
    if operation=='/':
        c=a/b
        print(c)
    if operation=='^':
        c=a*a
        d=b*b
        print('A^2='+str(c), 'B^2='+str(d))
    if operation=='√':
        c=math.sqrt(a)
        d=math.sqrt(b)
        print('√A='+str(c), '√B='+str(d))
    if operation=='V':
        print('🧡🧡🧡🧡🧡🧡🧡🧡🧡🧡')
        print('🧡  No "V", only "√"  🧡')
        print('🧡🧡🧡🧡🧡🧡🧡🧡🧡🧡')
