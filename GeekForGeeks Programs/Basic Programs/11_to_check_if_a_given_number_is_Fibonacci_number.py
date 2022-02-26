'''
Examples : 

Input : 8
Output : Yes

Input : 34
Output : Yes

Input : 41
Output : No
Following is an interesting property about Fibonacci numbers 
that can also be used to check if a given number is Fibonacci or not.

A number is Fibonacci if and only if one or both 
of (5*n2 + 4) or (5*n2 – 4) is a perfect square 
'''
import math

def isPerfectSquare(x):
    s=int(math.sqrt(x))
    return s*s==x

def isFibonacci(n):
    return isPerfectSquare(5*n*n+4) or isPerfectSquare(5*n*n-4)

for i in range(1,111):
    if(isFibonacci(i)==True):
        print(i," is a Fibonacci number")
    else:
        print(i," is not a Fibonacci number")