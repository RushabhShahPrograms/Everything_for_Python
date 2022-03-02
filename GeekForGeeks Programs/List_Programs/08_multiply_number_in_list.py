#normal method
def multiplyList(myList) :
     
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x
    return result
     
# Driver code
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print("Normal method")
print(multiplyList(list1))
print(multiplyList(list2))
print("\n")

#using numpy
import numpy

list1=[1,2,3]
list2=[4,5,6]

r1=numpy.prod(list1)
r2=numpy.prod(list2)

print("Using Numpy \nProduct of list1: {0} \nProduct of list2: {1}".format(r1,r2))
print("\n")


#using lambda
from functools import reduce

list1=[1,9,3]
list2=[4,5,5]

result1 = reduce((lambda x, y: x * y), list1)
result2 = reduce((lambda x, y: x * y), list2)
print("Using Lambda \nProduct of list1: {0} \nProduct of list2: {1}".format(r1,r2))
print("\n")

#using math
import math
list1 = [1, 2, 3]
list2 = [3, 2, 4]
 
 
result1 = math.prod(list1)
result2 = math.prod(list2)
print("using math")
print(result1)
print(result2)