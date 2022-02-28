'''
Given an array arr[] of n elements, write a function to search a given element x in arr[].
'''

def search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1

arr = [10,20,40,50,60,70,80,110,120,130,190,200]
x = 80
print("Output: ",search(arr,x))