'''
This is basically a variation of bubble-sort. This algorithm is divided into two phases- Odd and Even Phase. The algorithm runs until the array elements are sorted and in each iteration two phases occurs- Odd and Even Phases.

In the odd phase, we perform a bubble sort on odd indexed elements and in the even phase, we perform a bubble sort on even indexed elements.
'''

def bricksort(arr,n):
    issorted=0
    while issorted==0:
        issorted=1
        temp=0
        for i in range(1,n-1,2):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                issorted=0

        for i in range(0,n-1,2):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                issorted=0
    return

arr=[34,2,10,-9]
n=len(arr)
bricksort(arr,n);
for i in range(0,n):
    print(arr[i],end=" ")