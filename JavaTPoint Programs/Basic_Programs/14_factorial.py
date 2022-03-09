'''
n! = n* (n-1) * (n-2) *........1  
4! = 4x3x2x1 = 24    
'''
#normal method
num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial) 


#using math
import math  
def fact(n):  
    return(math.factorial(n))  
  
num = int(input("Enter the number:"))  
f = fact(num)  
print("Factorial of", num, "is", f)  
