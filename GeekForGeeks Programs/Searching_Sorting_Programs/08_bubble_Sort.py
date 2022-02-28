def bubble_sort(arr):
    for i in range(0,len(arr)-1):
        for j in range(len(arr)-1):
            if(arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr


arr=[65,78,12,45,1,90,23,67,29]
print("The sorted list is: ",bubble_sort(arr))