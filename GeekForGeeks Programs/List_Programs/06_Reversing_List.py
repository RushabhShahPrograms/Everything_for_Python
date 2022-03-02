def reverselist(lst,lst1):
    lst.reverse()
    new_lst=lst1[::-1]
    return (lst,new_lst)

lst=[1,2,3,4,5,6,7]
lst1=[11,12,13,14,15,16,17]
print(reverselist(lst,lst1))

