def enterCard(text):
    enter_string = str(input(text))
    #first_index=enter_string[4]
    #second_index=enter_string[9]
    #third_index=enter_string[14]
    if enter_string[4]==" " and enter_string[9]==" " and enter_string[14]==" ":
        return enter_string
    elif enter_string[4]=="" and enter_string[9]=="" and enter_string[14]=="":
        return "error"
    else:
        strings=' '.join(enter_string[i*4:(i+1)*4] for i in range(4))
        return strings

def bankcard(enter_strings):
    if len(enter_strings)==19 or len(enter_strings)==16:
        print("Bank card: " + enter_strings)
        index=enter_strings[0]
        if index=="4":
            return "Visa"
        if index=="5":
            return "MasterCard"
        if index=="3":
            return "Amex"
        if index=="0" or index=="1" or index=="2" or index=="6" or index=="7" or index=="8" or index=="9":
            return "Invalid card"
    else:
        print("Enter card number again")

def resultcard():
    print("This card is: " + str(bankcard(enterCard("Enter the card with a space: "))))

resultcard()