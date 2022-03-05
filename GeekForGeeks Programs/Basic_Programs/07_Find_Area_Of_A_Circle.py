from calendar import c


def findarea(pi,a):
    c=pi*a*a
    return c

pi=3.14
a=int(input("Enter the number to find area of circle: "))
print("Area of circle is: ",findarea(pi,a))