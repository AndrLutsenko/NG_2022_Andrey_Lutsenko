print("Enter value")
value=int(input())
print("Result:")
for i in range(value, 0, -1): #column value, 0, step(-1)
    for j in range(i, 0, -1): #initial element, Increment string to nth number, stride(-1)
        print(j, end=' ')
    print('')