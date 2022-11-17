import random

massiv=int(input("Введіть кількість елементів масиву: "))
n=[random.randint(1,50) for i in range(massiv)]
print("Elements massiv: ", n)
dobutok = 1
 
def DDobutok(x):  
    global dobutok
    if x == len(n):
        return    
    dobutok  *= n[x]
    DDobutok(x+1)
 
DDobutok(0)
print('\nDobutok = ', dobutok)
