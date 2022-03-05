k=3
str="geeks for geeks"
string=[]
text=str.split(" ")
for x in text:
    if len(x)>k:
        string.append(x)
print(string)