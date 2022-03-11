A = [[5, 4, 3],  
         [2, 4, 6],  
         [4, 7, 9]]    
B = [[3, 2, 4],  
         [4, 3, 6],  
         [2, 7, 5]]  
# Using nested list method with zip in Python  
multiResult = [[sum(a * b for a, b in zip(Arow, Bcol))   
                       for Bcol in zip(*B)]  
                                for Arow in A]  
# Printing multiplication result in the output  
print("The multiplication result of matrix A and B is: ")  
for res in multiResult:  
    print(res)    