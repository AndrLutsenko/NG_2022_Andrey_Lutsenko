import pandas as pd

def enterstring():
    strings = str(input("Enter string: "))
    list_string=list(strings)
    return list_string

def operation(list_string):
    result=pd.value_counts(list_string)
    return result

def result():
    print(operation(enterstring()))

result()