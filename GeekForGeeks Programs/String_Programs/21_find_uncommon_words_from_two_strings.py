def uncommon(a,b):
    a=a.split()
    b=b.split()
    k=set(a).symmetric_difference(set(b))
    return k

a="apple banana fruits"
b="mango apple fruits"
print(list(uncommon(a,b)))