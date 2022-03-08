test_tuple = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))

print("The original tuple: ",str(test_tuple))

res=[{'key':sub[0],'value':sub[1],'id':sub[2]} for sub in test_tuple]

print("The converted dictionary: ",str(res))