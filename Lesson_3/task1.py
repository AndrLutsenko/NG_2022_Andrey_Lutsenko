def EnterValue(text):
    enter_value = int(input(text))
    return enter_value

def chooseoperation():
    operation=int(input("Enter operation:\n1.Sum(+)\n2.Subtraction(-)\n3.Multiplication(*)\n4.Division(/)\n5.Power(^)\n6.Root(√)\n"))
    return operation

def operation(first,second,code):
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
            return "SQRT first element= " + str(first**0.5), "SQRT second element= " + str(second**0.5)

def result():
    first_value=EnterValue("Enter first value: ")
    second_value=EnterValue("Enter second value: ")
    print ("Result: " + str(operation(first_value,second_value,chooseoperation())))

result()