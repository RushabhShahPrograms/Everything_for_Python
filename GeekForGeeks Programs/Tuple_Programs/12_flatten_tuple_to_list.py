test_tuple=([5,6],[6,7,8,9],[3])
print("The original tuple: ",str(test_tuple))

res=tuple(sum(test_tuple, []))
print("The flattened tuple: ",str(res))