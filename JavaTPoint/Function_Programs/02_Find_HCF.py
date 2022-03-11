from re import X
from tkinter import Y


def calculate_hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=X
    for i in range(1,smaller+1):
        if((x%i==0) and (y%i==0)):
            hcf=i
    return hcf

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
print("The HCF of ",num1," and ",num2," is ",calculate_hcf(num1,num2))