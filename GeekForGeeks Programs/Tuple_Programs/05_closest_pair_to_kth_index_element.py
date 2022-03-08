test_list = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]
print("The original list is : " + str(test_list))
tup = (17, 23)
 
K = 1

min_dif, res = 999999999, None
for idx, val in enumerate(test_list):
    dif = abs(tup[K - 1] - val[K - 1])
    if dif < min_dif:
        min_dif, res = dif, idx
 
print("The nearest tuple to Kth index element is : " + str(test_list[res]))