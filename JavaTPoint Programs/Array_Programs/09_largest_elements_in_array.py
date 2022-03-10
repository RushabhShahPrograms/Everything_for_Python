arr=[25,11,34,78,23]
max=arr[0]
for i in range(0,len(arr)):
    if(arr[i]>max):
        max=arr[i]

print("Largest element present in given array: ",str(max))