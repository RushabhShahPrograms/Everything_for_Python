def returnSum(dict):
    sum=0
    for i in dict:
        sum+=dict[i]
    
    return sum

dict={'a':100,'b':200,'c':300}
print("Sum: ",returnSum(dict))