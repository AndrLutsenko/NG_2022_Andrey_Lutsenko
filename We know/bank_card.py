def enterCard(text):
    enter_string = str(input(text))
    return enter_string

def bankcard(enter_strings):
    if len(enter_strings)==19:
        print("Bank card: " + enter_strings)
        index=enter_strings[0]
        if index=="4":
            #print("This card is: Visa" + str(EnterValue("Enter the card with a space: ")))
            return "Visa"
        if index=="5":
            #print("This card is: MasterCard" + str(EnterValue("Enter the card with a space: ")))
            return "MasterCard"
        if index=="3":
            #print("This card is: Amex" + str(EnterValue("Enter the card with a space: ")))
            return "Amex"
        if index=="0" or index=="1" or index=="2" or index=="6" or index=="7" or index=="8" or index=="9":
            #print("Invalid card" + str(EnterValue("Enter the card with a space: ")))
            return "Invalid card"
    else:
        print("Enter card number again")

def resultcard():
    print("This card is: " + str(bankcard(enterCard("Enter the card with a space: "))))

resultcard()
#enter_string.index(0)        
#print(first_index)
#first_index=enter_string.index(0)
#if index==0:
#    print("Visa")

#if enter_string.index(1)=="1234":
 #   print("Visa")
#item=int(input("Введите номер елемента: "))
#print(enter_string[item])