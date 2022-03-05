from collections import Counter
test="GeeksForGeeks"
print("The original string is: ",test)
res=Counter(test)
res=max(res,key=res.get)
print("The minimum of all characters in GeeksforGeeks is: ",str(res))
