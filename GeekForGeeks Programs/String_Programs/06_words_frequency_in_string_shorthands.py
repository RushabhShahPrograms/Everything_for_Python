from collections import Counter

test = 'Gfg is best . Geeks are good and Geeks like Gfg'
print("The original string is: ",str(test))
res=Counter(test.split())
print("The words frequency: ",str(dict(res)))