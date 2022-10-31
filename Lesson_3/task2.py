def enterString(text):
    enter_string = str(input(text))
    return enter_string

def sortString(sorts):
    sort1=list(sorts)
    sort1.sort()
    return sort1
def resultsort():
    print ("Result: " + str(sortString(enterString("Your String: "))))

section=str(input("Menu: \n1. String sort\n2. Quantity of elements\n3. Vowels and consonants\n4. Partition and reverse\n5. World by number\n6. Enter string again\n7. Exit\nChoose a section:\n"))

if section=='1':
    resultsort()

#if section=="2":
    #def QuantityElements():
#if section=="3":
    #def VowelsAndConsonants():
#if section=="4":
    #def PartitionAndReverse():
#if section=="5":
    #def WorldByNumber():
if section=="6":
    def EnterStringRe():
        enter_string = input()
        return enter_string
    EnterStringRe()
if section=="7":
    def exit():
        exit