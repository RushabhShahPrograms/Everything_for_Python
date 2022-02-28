def cyclesort(array):
    writes=0

    for cyclestart in range(0,len(array)-1):
        item=array[cyclestart]

        pos=cyclestart
        for i in range(cyclestart+1,len(array)):
            if(array[i]<item):
                pos=pos+1

        if(pos==cyclestart):
            continue

        while(item==array[pos]):
            pos=pos+1
        array[pos],item=item,array[pos]
        writes=writes+1

        while(pos!=cyclestart):
            pos=cyclestart
            for i in range(cyclestart+1,len(array)):
                if(array[i]<item):
                    pos=pos+1
                    
            while(item==array[pos]):
                pos=pos+1
            array[pos],item=item,array[pos]
            writes=writes+1
    return writes


arr=[1,7,6,9,2,67,23]
n=len(arr)
cyclesort(arr)
print("After sort: ")
for i in range(0,n):
    print(arr[i],end=" ")
