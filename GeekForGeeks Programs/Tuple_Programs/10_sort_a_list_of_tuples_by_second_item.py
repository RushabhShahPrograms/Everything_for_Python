def sort_tuple(tup):
    return(sorted(tup,key=lambda x: x[1]))

tup=[('rishav',10),('jai',2),('kartik',7),('ram',1),('akash',3)]
print(sort_tuple(tup))