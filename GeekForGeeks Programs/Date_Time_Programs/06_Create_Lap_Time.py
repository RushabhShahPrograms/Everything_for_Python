import time
starttime=time.time()
lasttime=starttime
lapnum=1

print("Press ENTER to count laps. \n Press CTRL+c to stop")

try:
    while True:
        input()
        laptime=round((time.time()-lasttime),2)
        totaltime=round((time.time()-starttime),2)

        print("Lap no. "+str(lapnum))
        print("Total Time: ",str(totaltime))
        print("Lap Time: ",str(laptime))

        print("*"*20)

        lasttime=time.time()
        lapnum+=1

except KeyboardInterrupt:
    print("Done")
    