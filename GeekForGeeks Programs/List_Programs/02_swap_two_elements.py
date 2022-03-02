def swapposition(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list

list=[5,7,45,78,12,90]
pos1,pos2=1,3
print(swapposition(list,pos1,pos2))