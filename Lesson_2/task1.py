str=input("Enter string: ")

lists=list(str)
result = dict((i, lists.count(i)) for i in lists )
for key in sorted(result):
    print(key,result[key])