English_alfavit="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
step=int(input("Encryption step: ")) #step 13 for message
message=input("Message to decrypt: ").upper()
result=""
for i in message:
        position=English_alfavit.find(i)
        new_position = position+step
        if i in English_alfavit:
            result+=English_alfavit[new_position]
        else:
             result += i
print("\n",result)