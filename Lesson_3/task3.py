lists=input("")
result = {i: lists.count(i) for i in set(lists) }
print(result)