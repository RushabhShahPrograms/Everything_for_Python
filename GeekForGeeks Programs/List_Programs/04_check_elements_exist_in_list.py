test=[34,78,12,90,2,4,6,8]

print("Checking 2 exists in list using for loop: ")
for i in test:
    if i==2:
        print("Elements exists")


print("Checking 4 exists in list using in operator: ")
if(4 in test):
    print("Element exists")
