'''
Input : n = 5
Output : 225
13 + 23 + 33 + 43 + 53 = 225
'''

n=5
sum=0
for i in range(1,n+1):
    sum+=i*i*i
print(sum)