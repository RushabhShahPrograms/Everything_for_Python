'''
Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.
'''

def insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key <arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=key

arr = [11,12,45,8,3]
insertionsort(arr)
print("Sorted array: ")
for i in range(len(arr)):
    print(arr[i],sep=" ")