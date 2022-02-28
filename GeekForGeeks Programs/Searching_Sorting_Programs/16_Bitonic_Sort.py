'''
It mainly involves two steps.  

Forming a bitonic sequence (discussed above in detail). After this step we reach the fourth stage in below diagram, i.e., the array becomes {3, 4, 7, 8, 6, 5, 2, 1}
Creating one sorted sequence from bitonic sequence: After first step, first half is sorted in increasing order and second half in decreasing order. 
We compare first element of first half with first element of second half, then second element of first half with second element of second and so on. We exchange elements if an element of first half is smaller. 
After above compare and exchange steps, we get two bitonic sequences in array. See fifth stage in below diagram. In the fifth stage, we have {3, 4, 2, 1, 6, 5, 7, 8}. If we take a closer look at the elements, we can notice that there are two bitonic sequences of length n/2 such that all elements in first bitonic sequence {3, 4, 2, 1} are smaller than all elements of second bitonic sequence {6, 5, 7, 8}. 
We repeat the same process within two bitonic sequences and we get four bitonic sequences of length n/4 such that all elements of leftmost bitonic sequence are smaller and all elements of rightmost. See sixth stage in below diagram, arrays is {2, 1, 3, 4, 6, 5, 7, 8}. 
If we repeat this process one more time we get 8 bitonic sequences of size n/8 which is 1. Since all these bitonic sequence are sorted and every bitonic sequence has one element, we get the sorted array.
'''

#main part
def compAndSwap(a,i,j,dire):
    if(dire==1 and a[i]>a[j] or (dire==0 and a[i]>a[j])):
        a[i],a[j]=a[j],a[i]

def bitonicmerge(a,low,cnt,dire):
    if cnt>1:
        k=cnt//2
        for i in range(low,low+k):
            compAndSwap(a,i,i+k,dire)
        bitonicmerge(a,low,k,dire)
        bitonicmerge(a,low+k,k,dire)

def bitonicsort(a,low,cnt,dire):
    if cnt>1:
        k=cnt//2
        bitonicsort(a,low,k,1)
        bitonicsort(a,low+k,k,0)
        bitonicmerge(a,low,cnt,dire)

def sort(a,N,up):
    bitonicsort(a,0,N,up)

#Driver Code
a = [3,7,4,8,6,2,1,5]
n = len(a)
up = 1

sort(a,n,up)
print("Sorted array is: ")
for i in range(n):
    print("%d"%a[i],end=" ")