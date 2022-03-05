def revword(input):
    words=input.split(' ')
    revword=' '.join(reversed(words))
    return revword


#Driver code
input = 'geeks contest of code india code'
print(revword(input))