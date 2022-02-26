'''
In mathematical terms, the sequence Fn of 
Fibonacci numbers is defined by the recurrence relation 

Fn = Fn-1 + Fn-2
With seed values 

F0 = 0 and F1 = 1.
'''

def Fibonacci(n):
    if n<=0:
        print("Incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

n=int(input("Enter the nth value to print fibonacci series: "))
print(Fibonacci(n))