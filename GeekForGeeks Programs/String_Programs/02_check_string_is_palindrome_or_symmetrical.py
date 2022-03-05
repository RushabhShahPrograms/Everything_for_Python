def palindrome(string):
    mid=(len(string)-1)//2
    start=0
    last=len(string)-1
    flag=0

    while(start<=mid):
        if string[start]==string[last]:
            start += 1
            last -= 1

        else:
            flag=1
            break

    if flag==0:
        print("The entered string is palindrome")
    else:
        print("The entered string is not palindrome")


def symmetry(string):
    n=len(string)
    flag=0

    if n%2:
        mid=n//2+1
    else:
        mid=n//2

    start1=0
    start2=mid

    while(start1<mid and start2<n):
        if string[start1]==string[start2]:
            start1 += 1
            start2 += 1
        else:
            flag=1
            break

    if flag==0:
        print("The entered string symmetrical")
    else:
        print("The entered string is not symmetrical")


#Driver code
string="aa"
palindrome(string)
symmetry(string)