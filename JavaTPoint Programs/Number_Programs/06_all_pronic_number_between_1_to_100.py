'''
The pronic number is a product of two consecutive integers of the form: n(n+1).

For example:

6 = 2(2+1)= n(n+1),
72 =8(8+1) = n(n+1)

Some pronic numbers are: 0, 2, 6, 12, 20, 30, 42, 56 etc.
'''

def isPronicNumber(num):
    flag=False
    for j in range(1,num+1):
        if((j*(j+1)) == num):
            flag = True
            break
    return flag

print("Pronic numbers between 1 and 100: ")    
for i in range(1, 101):    
    if(isPronicNumber(i)):    
        print(i,end=" ")