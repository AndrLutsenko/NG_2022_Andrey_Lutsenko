import math

def EnterValue(text):
    enter_value = int(input(text))
    return enter_value

def main():
    operation=str(input("Enter an operation +,-,*,/,^,√: "))

    if operation=='+':
        def SumElements(first_element_for_sum, second_element_for_sum):
             return first_element_for_sum + second_element_for_sum

        def processAndShowPowerNumber():
            print ("Result: " + str(SumElements(EnterValue("Enter first value: "),EnterValue("Enter second value: "))))
        
        processAndShowPowerNumber()

    if operation=='-':
        def MinusElements(first_element_for_minus, second_element_for_minus):
            return first_element_for_minus - second_element_for_minus

        def processAndShowPowerNumber():
            print ("Result: " + str(MinusElements(EnterValue("Enter first value: "),EnterValue("Enter second value: "))))
        
        processAndShowPowerNumber()

    if operation=='*':
        def MultiplicationElements(first_element_for_multiplication, second_element_for_multiplication):
            return first_element_for_multiplication * second_element_for_multiplication

        def processAndShowPowerNumber():
            print ("Result: " + str(MultiplicationElements(EnterValue("Enter first value: "),EnterValue("Enter second value: "))))
        
        processAndShowPowerNumber()

    if operation=='/':
        def DivisionElements(first_element_for_division, second_element_for_division):
            return first_element_for_division / second_element_for_division

        def processAndShowPowerNumber():
            print ("Result: " + str(DivisionElements(EnterValue("Enter first value: "),EnterValue("Enter second value: "))))
        
        processAndShowPowerNumber()

    if operation=='^':
        def DegreeElements(first_element_for_degree, second_element_for_degree):
             return first_element_for_degree ** second_element_for_degree

        def processAndShowPowerNumber():
            print ("Result: " + str(DegreeElements(EnterValue("Enter first value: "),EnterValue("Enter second value: "))))
        
        processAndShowPowerNumber()

    if operation=='√':
        def SQRTElements(first_element_for_sqrt, second_element_for_sqrt):
            return "Root first element= " + str(math.sqrt(first_element_for_sqrt)), "Root second element= " + str(math.sqrt(second_element_for_sqrt)) 

        def processAndShowPowerNumber():
            print ("Result: " + str(SQRTElements(EnterValue("Enter first value: "),EnterValue("Enter second value: "))))
        
        processAndShowPowerNumber()

main()