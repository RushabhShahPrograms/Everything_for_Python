'''
Pigeonhole sorting is a sorting algorithm that is suitable for sorting lists of elements where the number of elements and the number of possible key values are approximately the same.
It requires O(n + Range) time where n is number of elements in input array and \’Range\’ is number of possible values in array.

Working of Algorithm :

Find minimum and maximum values in array. Let the minimum and maximum values be \’min\’ and \’max\’ respectively. Also find range as \’max-min-1\’.
Set up an array of initially empty “pigeonholes” the same size as of the range.
Visit each element of the array and then put each element in its pigeonhole. An element arr[i] is put in hole at index arr[i] – min.
Start the loop all over the pigeonhole array in order and put the elements from non- empty holes back into the original array.
'''

def pigeonholesort(a):
    my_min=min(a)
    my_max=max(a)
    size=my_max-my_min+1
    holes=[0]*size

    for x in a:
        assert type(x) is int, "integers only please"
        holes[x-my_min]=holes[x-my_min]+1
    
    i=0
    for count in range(size):
        while holes[count]>0:
            holes[count]=holes[count]-1
            a[i]=count+my_min
            i=i+1


a = [8,7,2,5,4,1,9,12]
print("Sorted order is: ",end=" ")
pigeonholesort(a)
for i in range(0,len(a)):
    print(a[i],end=" ")