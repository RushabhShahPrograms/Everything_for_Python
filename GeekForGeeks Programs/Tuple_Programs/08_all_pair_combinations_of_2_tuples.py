tuple1=(4,5)
tuple2=(7,8)

print("The original tuple 1: ",str(tuple1))
print("The original tuple 2: ",str(tuple2))

res=[(a,b) for a in tuple1 for b in tuple2]
res=res+[(a,b) for a in tuple2 for b in tuple1]

print("The filtered tuple: ",str(res))