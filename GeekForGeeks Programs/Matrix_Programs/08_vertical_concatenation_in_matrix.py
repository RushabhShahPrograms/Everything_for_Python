from itertools import zip_longest

test_list=[["gfg","good"],["is","for"],["best"]]

res = ["".join(ele) for ele in zip_longest(*test_list, fillvalue ="")]

print("list after column concatenation: ",str(res))