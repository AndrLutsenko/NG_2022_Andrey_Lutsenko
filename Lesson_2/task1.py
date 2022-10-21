#Алгоритмы и структуры данных Лабораторна робота 1 -> Задание 2
import random
x=int(input("Введіть кількість елементів масиву"))
n=[random.randint(1,50) for i in range(x)]
print(n)
c=1
for i in range(x):
    c*=n[i]
    print(c)
