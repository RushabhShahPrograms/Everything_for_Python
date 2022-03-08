from collections import OrderedDict

def kthrepeating(input,k):
    dict=OrderedDict.fromkeys(input,0)

    for ch in input:
        dict[ch]+=1

    nonRepreatDict=[key for (key,value) in dict.items() if value==1]

    if len(nonRepreatDict)<k:
        return 'Less than k non-repeating characters in input.'
    else:
        return nonRepreatDict[k-1]

input = "geeksforgeeks"
k = 3
print (kthrepeating(input, k)) 