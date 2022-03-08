test_dict = {"Gfg" : 1, "is" :  3, "Best" : 2}

print("The original dictionary is : " + str(test_dict))

res = list(test_dict.keys()) + list(test_dict.values())

print("The ordered keys and values : " + str(res)) 