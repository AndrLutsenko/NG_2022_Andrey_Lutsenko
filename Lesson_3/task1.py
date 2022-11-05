import math
def EnterValue(text):
    enter_value = int(input(text))
    return enter_value

def operation(first,second):
    operation=str(input("Enter an operation +,-,*,/,^,√: "))
    if operation=="+":
        return first+second

    if operation=="-":
        return first-second

    if operation=="*":
        return first*second
    
    if operation=="/":
        return first/second

    if operation=="^":
        return first**second

    if operation=="√":
        return "First element sqrt= " + str(math.sqrt(first)), "Second element sqrt= " + str(math.sqrt(second))

def result():
    print ("Result: " + str(operation(EnterValue("Enter first value: "),EnterValue("Enter second value: "))))

result()