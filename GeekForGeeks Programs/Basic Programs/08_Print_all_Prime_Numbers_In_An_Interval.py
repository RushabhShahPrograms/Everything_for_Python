'''
Given two positive integers start and end. 
The task is to write a Python program to 
print all Prime numbers in an Interval.

Definition: A prime number is a natural number 
greater than 1 that has no positive divisors other than
 1 and itself. 
The first few prime numbers are {2, 3, 5, 7, 11, ….}.
'''
def prime(x,y):
    prime_lst=[]
    for i in range(x,y):
        if i==0 or i==1:
            continue
        else:
            for j in range(2,int(i/2)+1):
                if i%j==0:
                    break
            else:
                prime_lst.append(i)
    return prime_lst
start=2
end=7
lst=prime(start,end)
if len(lst)==0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ",lst)