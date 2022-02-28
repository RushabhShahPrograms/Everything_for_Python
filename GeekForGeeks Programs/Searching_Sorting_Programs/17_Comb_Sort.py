'''
Comb Sort is mainly an improvement over Bubble Sort. Bubble sort always compares adjacent values. So all inversions are removed one by one. Comb Sort improves on Bubble Sort by using gap of size more than 1. The gap starts with a large value and shrinks by a factor of 1.3 in every iteration until it reaches the value 1. Thus Comb Sort removes more than one inversion counts with one swap and performs better than Bubble Sort.
The shrink factor has been empirically found to be 1.3 

Although, it works better than Bubble Sort on average, worst case remains O(n2). 
'''

#main part
def get_gap(gap):

    gap = (gap * 10)/13

    if gap < 1:

        return 1

    gap = int(gap)

    return gap




def sort(arr, length):

    gap = length

    is_swapped = True

    while gap != 1 or is_swapped == 1:

        gap = get_gap(gap)

        is_swapped = False

        for i in range(0, length - gap):

            if arr[i] > arr[i + gap]:

                arr[i], arr[i + gap] = arr[i + gap], arr[i]

                is_swapped = True

       

ip_arr = [51, 2, -14, -6, 3]

sort(ip_arr, len(ip_arr))

print("The sorted array is ")

for i in range(len(ip_arr)):

    print(ip_arr[i])