test=(5, 20, 3, 7, 6, 8)
print("The original tuple is: ",str(test))

k=2

test=list(test)
temp=sorted(test)
res=tuple(temp[:k]+temp[-k:])
print("The extracted values: ",str(res))