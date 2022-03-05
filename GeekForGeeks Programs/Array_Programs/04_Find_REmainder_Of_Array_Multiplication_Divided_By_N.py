from functools import reduce

def find_remainder(arr,n):
    sum1=reduce(lambda x,y:x*y,arr)
    remainder=sum1%n
    print("Remainder is: ",remainder)

arr=[100,10,5,25,35,14]
n=11
find_remainder(arr,n)
