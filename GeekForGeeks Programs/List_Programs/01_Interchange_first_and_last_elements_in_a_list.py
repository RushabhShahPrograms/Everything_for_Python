#using temp

def swaplist(newlist):
    size=len(newlist)
    
    temp=newlist[0]
    newlist[0]=newlist[size-1]
    newlist[size-1]=temp

    return newlist

newlist=[12,35,7,9,23]
print(swaplist(newlist))



#without temp

def swap(newlist1):
    newlist1[0],newlist1[-1]=newlist1[-1],newlist1[0]
    return newlist1

newlist1=[34,78,9,12,9]
print(swap(newlist1))
