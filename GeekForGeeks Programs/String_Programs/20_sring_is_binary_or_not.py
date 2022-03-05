def check(string):
    t='01'
    count=0
    for char in string:
        if char not in t:
            count=1
            break
        else:
            pass

    if count:
        print("No")
    else:
        print("Yes")

string="00011101010101110011"
check(string)