'''
Formula to calculate compound interest annually is given by: 
A = P(1 + R/100) t 
Compound Interest = A – P 
Where, 
A is amount 
P is principle amount 
R is the rate and 
T is the time span
'''

def CI(principle,rate,time):
    Amount=principle*(pow((1+rate/100),time))
    ci=Amount-principle
    print("Compound Interest is ",ci)

principle = 10000
rate = 10.25
time = 5
CI(principle,rate,time)