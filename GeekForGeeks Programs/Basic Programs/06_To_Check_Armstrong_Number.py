def isArmstrong(x):
    temp=x
    sum=0
    while(temp!=0):
        r=temp%10
        sum=sum+r*r*r
        temp=temp//10
    return (sum==x)

x=int(input("Enter the number to check armstrong or not: "))
print(isArmstrong(x))