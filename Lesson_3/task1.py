import math

def EnterValue(text):
    enter_value = int(input(text))
    return enter_value

def SumElements(first_element_for_sum, second_element_for_sum):
    return first_element_for_sum + second_element_for_sum

def processAndShowPowerNumberSum():
    print ("Result: " + str(SumElements(EnterValue("Enter first value: "),EnterValue("Enter second value: "))))

def MinusElements(first_element_for_minus, second_element_for_minus):
    return first_element_for_minus - second_element_for_minus

def processAndShowPowerNumberMinus():
    print ("Result: " + str(MinusElements(EnterValue("Enter first value: "),EnterValue("Enter second value: "))))

def MultiplicationElements(first_element_for_multiplication, second_element_for_multiplication):
    return first_element_for_multiplication * second_element_for_multiplication

def processAndShowPowerNumberMultiplication():
    print ("Result: " + str(MultiplicationElements(EnterValue("Enter first value: "),EnterValue("Enter second value: "))))

def DivisionElements(first_element_for_division, second_element_for_division):
    return first_element_for_division / second_element_for_division

def processAndShowPowerNumberDivision():
    print ("Result: " + str(DivisionElements(EnterValue("Enter first value: "),EnterValue("Enter second value: "))))

def DegreeElements(first_element_for_degree, second_element_for_degree):
    return first_element_for_degree ** second_element_for_degree

def processAndShowPowerNumberDegree():
    print ("Result: " + str(DegreeElements(EnterValue("Enter first value: "),EnterValue("Enter second value: "))))

def SQRTElements(first_element_for_sqrt, second_element_for_sqrt):
    return "Root first element= " + str(math.sqrt(first_element_for_sqrt)), "Root second element= " + str(math.sqrt(second_element_for_sqrt)) 

def processAndShowPowerNumberSQRT():
    print ("Result: " + str(SQRTElements(EnterValue("Enter first value: "),EnterValue("Enter second value: "))))

operation=str(input("Enter an operation +,-,*,/,^,√: "))

if operation=='+':
    processAndShowPowerNumberSum()

if operation=='-': 
    processAndShowPowerNumberMinus()

if operation=='*':
    processAndShowPowerNumberMultiplication()

if operation=='/':          
    processAndShowPowerNumberDivision()

if operation=='^':        
    processAndShowPowerNumberDegree()

if operation=='√':            
    processAndShowPowerNumberSQRT()