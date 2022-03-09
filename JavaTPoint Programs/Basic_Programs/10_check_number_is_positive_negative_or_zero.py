def checknumber(a):
    if a>0:
        print("Positive")
    elif a<0:
        print("Negative")
    else:
        print("Zero")

a=float(input("Enter a number as input value: "))
checknumber(a)