def remove(string,i):
    a=string[ :i]
    b=string[i+1: ]
    return a+b

string="geeksforGeeks"
i=5
print(remove(string,i))