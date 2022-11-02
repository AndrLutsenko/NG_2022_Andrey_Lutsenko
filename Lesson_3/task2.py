def enterString(text):
    enter_string = str(input(text))
    return enter_string

def sortString(sorts):
    sort1=list(sorts)
    sort1.sort()
    return sort1

def resultsort():
    print ("Sorted string: " + str(sortString(enterString("Your String: "))))

def quantityElements(sorts):
    s_string = set(sorts) #non-repeating elements
    summ = [] #Summation of elements
    for s_symbol in s_string:
        count = 0
        for symbol in sorts:
            if s_symbol == symbol:
                count += 1
        summ.append(f'{s_symbol}= {count}')
    return summ

def resultQuantity():
    print ("Quantity elements: " + str(quantityElements(enterString("Your String: "))))

def VowelsAndConsonants(letter):
    result1 = set()
    result2 = set()
    for lettVowels in letter:
        if lettVowels in 'aeiouyAEIOUY':
            result1.add(lettVowels)
    for lettConsonants in letter:
        if lettConsonants in 'qwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNM':
            result2.add(lettConsonants)
    return result1, result2

def resultVowelsAndConsonants():
    print ("Vowelc and Consonants: " + str(VowelsAndConsonants(enterString("Your String: "))))

def PartitionAndReverse(partition_and_reverse):
    partition_and_reverse=partition_and_reverse.split(" ")
    partition_and_reverse.reverse()
    return partition_and_reverse

def resultPartitionAndReverse():
    print ("Partition and Reverse: " + str(PartitionAndReverse(enterString("Your String: "))))
    
def WorldByNumber(lists):
    listss=list(lists.split(" "))
    print(listss)
    item=int(input("Введите номер елемента: "))
    return listss[item]

def resultWorldByNumber():
    print ("World by number: " + str(WorldByNumber(enterString("Your String: "))))

def resultPrint():
    print ("Resulting string: " + str(enterString("Your String: ")))
    print ("Do you want to re-enter the line? Yes/No")
    interview=input()
    if interview=="Yes" or interview=="yes":
        print ("Resulting string: " + str(enterString("Your String: ")))
    if interview=="No" or interview=="no":
        exit

def exitProgram():
        exit

section=str(input("Menu: \n1. String sort\n2. Quantity of elements\n3. Vowels and consonants\n4. Partition and reverse\n5. World by number\n6. Enter string again\n7. Exit\nChoose a section:\n"))

if section=='1':
    resultsort()

if section=="2":
    resultQuantity()

if section=="3":
    resultVowelsAndConsonants()
if section=="4":
    resultPartitionAndReverse()
if section=="5":
    resultWorldByNumber()
if section=="6":
    resultPrint()
if section=="7":
    exitProgram()