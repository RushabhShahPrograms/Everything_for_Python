def divide_chunks(l,n):
    for i in range(0,len(l),n):
        yield l[i:i+n]

my_list=['rushabh','shah',
'learning','more','about','python',
'from','geeks','for','geeks']
n=5
x=list(divide_chunks(my_list,n))
print(x)