test="geeksforgeeks"
print("The original string is: ",test)

temp=str.maketrans("geek","abcd")
temp_str=test.translate(temp)

print("The string after swap: ",str(temp_str))