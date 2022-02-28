'''
BogoSort also known as permutation sort, stupid sort, slow sort, shotgun sort or monkey sort is a particularly ineffective algorithm based on generate and test paradigm. The algorithm successively generates permutations of its input until it finds one that is sorted.(Wiki) 
For example, if bogosort is used to sort a deck of cards, it would consist of checking if the deck were in order, and if it were not, one would throw the deck into the air, pick the cards up at random, and repeat the process until the deck is sorted. 

PseudoCode: 
 

while not Sorted(list) do
    shuffle (list)
done
'''

import random

def bogosort(a):
    n=len(a)
    while (issorted(a)==False):
        shuffle(a)


def issorted(a):
    n=len(a)
    for i in range(0,n-1):
        if(a[i]>a[i+1]):
            return False
    return True

def shuffle(a):
    n=len(a)
    for i in range(0,n):
        r=random.randint(0,n-1)
        a[i],a[r]=a[r],a[i]

a=[3,2,5,1,7,5,8,0]
bogosort(a)
print("Sorted array: ")
for i in range(len(a)):
    print("%d" %a[i])