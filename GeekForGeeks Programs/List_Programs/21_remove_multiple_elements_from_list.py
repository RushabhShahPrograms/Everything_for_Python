#Approach 1
list1 = [11, 5, 17, 18, 23, 50]

del list1[1:5]
 
print(*list1)


#Approach 2
list1 = [11, 5, 17, 18, 23, 50]

for ele in list1:
    if ele % 2 == 0:
        list1.remove(ele)

print("New list after removing all even numbers: ", list1)



#Approach 3
list1 = [11, 5, 17, 18, 23, 50]

list1 = [ elem for elem in list1 if elem % 2 != 0]
 
print(*list1)
