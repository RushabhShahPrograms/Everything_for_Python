'''
Python counter and dictionary intersection example (Make a string using deletion and rearrangement)
'''

from collections import Counter
  
def makeString(str1,str2):

    dict1 = Counter(str1)
    dict2 = Counter(str2)

    result = dict1 & dict2

    return result == dict1

if __name__ == "__main__":
    str1 = 'ABHISHEKsinGH'
    str2 = 'gfhfBHkooIHnfndSHEKsiAnG'
    if (makeString(str1,str2)==True):
        print("Possible")
    else:
        print("Not Possible")