def product(val):
    res=1
    for ele in val:
        res*=ele
    return res

test = [[1,4,5],[7,3],[4],[46,7,3]]
print("Original list: ",str(test))
res=product([ele for sub in test for ele in sub])

print("Total element product in lists is: ",str(res))