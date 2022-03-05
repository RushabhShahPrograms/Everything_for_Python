## initializing string
string = "geeksforgeeks"
## initializing a list to append all the duplicate characters
duplicates = []
for char in string:
   if string.count(char) > 1:
       if char not in duplicates:
           duplicates.append(char)

print(*duplicates)