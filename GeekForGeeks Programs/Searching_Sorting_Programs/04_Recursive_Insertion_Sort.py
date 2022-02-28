def insertionsortrecursive(arr,n):
    if n<=1:
        return

    insertionsortrecursive(arr,n-1)
    
    last = arr[n-1]
    j = n-2

    while(j>=0 and arr[j]>last):
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=last

arr = [-7,11,6,0,-3,5,10,2]
n = len(arr)
insertionsortrecursive(arr,n)
print(arr)