test='Geeksforgeeks is best for geeks and cs'
print("The original string is: ",str(test))
word_list=["best","cs"]
repl_word='gfg'
res=' '.join([repl_word if idx in word_list else idx for idx in test.split()])
print("String after multiple replace: ",str(res))