arr=[12,34,78,23,45]
n=len(arr)
max=arr[0]
for i in range(1,n):
    if arr[i]>max:
        max=arr[i]

print("Largest number in given array is: ",max)