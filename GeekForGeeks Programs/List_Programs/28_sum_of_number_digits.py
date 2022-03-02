'''
Method #1 : Using loop + str() 
This is brute force method to perform this particular task. 
In this, we run a loop for each element, convert each digit to string,
and perform the count of the sum of each digit.
'''

test_list = [12, 67, 98, 34]
 
# printing original list
print("The original list is : " + str(test_list))

res = []
for ele in test_list:
    sum = 0
    for digit in str(ele):
        sum += int(digit)
    res.append(sum)
     
# printing result
print("List Integer Summation : " + str(res))


'''
Method #2 : Using sum() + reduce()
This task can also be performed using shorthand using the above functionalities. 
The sum() is used to compute summation and reduce function from functools module.
'''

from functools import reduce
 
# Initializing list
test_list = [12, 67, 98, 34]
 
# printing original list
print("The original list is : " + str(test_list))

res = [reduce(lambda x, y: int(x) + int(y), list(str(i))) for i in test_list]
 
# printing result
print("List Integer Summation : " + str(res))