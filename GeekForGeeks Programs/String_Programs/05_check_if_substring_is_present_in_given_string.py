def check(s2,s1):
    if s2.count(s1)>0:
        print("yes")
    else:
        print("no")

s2 = "A geek in need is a geek indeed"
s1 = "geek"
check(s2,s1)