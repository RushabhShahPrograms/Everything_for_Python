import sys

a=[56,90,12,45,23,17]
for i in range(len(a)):
    min_idx=i
    for j in range(i+1,len(a)):
        if(a[min_idx]>a[j]):
            min_idx=j

a[i],a[min_idx]=a[min_idx],a[i]

print("Sorted array")
for i in range(len(a)):
    print(a[i])