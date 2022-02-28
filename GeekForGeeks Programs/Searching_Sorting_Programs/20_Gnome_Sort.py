def gnomeSort( arr, n):
   index = 0
   while index < n:
      if index == 0:
         index = index + 1
      if arr[index] >= arr[index - 1]:
         index = index + 1
      else:
         arr[index], arr[index-1] = arr[index-1], arr[index]
         index = index - 1
   return arr
# main
arr = [1,4,2,3,6,5,8,7]
n = len(arr)
arr = gnomeSort(arr, n)
print ("Sorted sequence is:")
for i in arr:
   print (i,end=" ")