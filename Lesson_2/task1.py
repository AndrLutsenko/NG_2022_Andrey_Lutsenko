import pandas as pd

strings = str(input("Enter string: "))
list_string=list(strings)
print(pd.value_counts(list_string))