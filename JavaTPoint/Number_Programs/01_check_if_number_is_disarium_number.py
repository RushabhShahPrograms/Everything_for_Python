'''
For example, 175 is a Disarium number as follows:

1^1+ 7^2 + 5^3 = 1+ 49 + 125 = 175
'''

def calculatelength(n):
    length=0
    while(n!=0):
        length=length+1
        n=n//10
    return length

num=175
rem=sum=0
len=calculatelength(num)

n=num

while(num>0):
    rem=num%10
    sum=sum+int(rem**len)
    num=num//10
    len=len-1

if(sum==n):
    print(str(n)+" is a disarium number")
else:
    print(str(n)+" is not a disarium number")