'''
In a nutshell, this search algorithm takes advantage of a collection of elements that is already sorted by ignoring half of the elements after just one comparison. 

Compare x with the middle element.
If x matches with the middle element, we return the mid index.
Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.
Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.
'''

def binarysearch(arr,low,high,x):
    if high >= low:
        mid = (high+low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binarysearch(arr,low,mid-1,x)
        else:
            return binarysearch(arr,mid+1,high,x)
    else:
        return -1


arr = [2,3,4,10,40]
x = 3
result=binarysearch(arr,0,len(arr)-1,x)
if result!=-1:
    print("Element is present at index ",str(result))
else:
    print("Element is not present in array")