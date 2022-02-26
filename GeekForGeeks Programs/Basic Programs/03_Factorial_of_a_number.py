#using math function

import math
def fact(n):
    return(math.factorial(n))

n=5
print("Factorial of {0} is {1}".format(n,fact(n)))


#doing simply

num = int(input("Enter the number: "))
if num<0:
    print("If value is less than zero then factorial is not possible")
elif num==0 or num==1:
    print("If value is 0 or 1 then answer is 1")
else:
    fact=1
    while(num>1):
        fact*=num
        num-=1
    print("Factorial is ",fact)