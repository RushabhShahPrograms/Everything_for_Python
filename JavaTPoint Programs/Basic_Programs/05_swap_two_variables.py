#using naive approach

P = int( input("Please enter value for P: "))  
Q = int( input("Please enter value for Q: "))  

temp_1 = P  
P = Q  
Q = temp_1  

print ("The Value of P after swapping: ", P)  
print ("The Value of Q after swapping: ", Q)  

#using comma operator

P = int( input("Please enter value for P: "))  
Q = int( input("Please enter value for Q: ")) 

P, Q = Q, P 

print ("The Value of P after swapping: ", P)  
print ("The Value of Q after swapping: ", Q)

#using XOR method

P = int( input("Please enter value for P: "))  
Q = int( input("Please enter value for Q: "))

P = P ^ Q  
Q = P ^ Q  
P = P ^ Q  

print ("The Value of P after swapping: ", P)  
print ("The Value of Q after swapping: ", Q) 

#arithmetic operator
# 1) add and sub

P = int( input("Please enter value for P: "))  
Q = int( input("Please enter value for Q: "))  
P = P + Q    
Q = P - Q   
P = P - Q  
   
print ("The Value of P after swapping: ", P)  
print ("The Value of Q after swapping: ", Q)

# 2) multiplication and division

P = int( input("Please enter value for P: "))  
Q = int( input("Please enter value for Q: "))  

P = P * Q    
Q = P / Q   
P = P / Q  
   
print ("The Value of P after swapping: ", P)  
print ("The Value of Q after swapping: ", Q)  