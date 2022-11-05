import math

def EnterValue(text):
    enter_value = int(input(text))
    return enter_value

def operation(first, second, code):
    match code:
        case 1:
            return first + second
        case 2:
            return first - second
        case 3:
            return first * second
        case 4:
            return first/second
        case 5:
            return first**second
        case 6:
            return "SQRT first element= " + str(math.sqrt(first)), "SQRT second element= " + str(math.sqrt(second))

def result():
    print ("Result: " + str(operation(EnterValue("Enter first value: "),EnterValue("Enter second value: "),EnterValue("Enter operation:\n1.Sum(+)\n2.Subtraction(-)\n3.Multiplication(*)\n4.Division(/)\n5.Power(^)\n6.Root(√)\n"))))

result()