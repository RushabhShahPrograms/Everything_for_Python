
x = [[1,2,3],[4,5,6]]
y = [[7,8,9],[1,2,3]]
result = [[0,0,0],[0,0,0]]
result1 = [[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j]=x[i][j]+y[i][j]

print("Addition: ")
for r in result:
    print(r)


for i in range(len(x)):
    for j in range(len(x[0])):
        result1[i][j]=x[i][j]-y[i][j]

print("Substraction: ")
for r1 in result1:
    print(r1)