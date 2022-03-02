test_list = [5, 6, [], 3, [], [], 9]
 
print("The original list is : " + str(test_list))

res = [ele for ele in test_list if ele != []]
print ("List after empty list removal : " + str(res))