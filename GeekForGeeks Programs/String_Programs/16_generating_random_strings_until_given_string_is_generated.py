import string
import random
import time

possible=string.ascii_lowercase+string.digits+string.ascii_uppercase+ ' ., !?;:@#$%^&*( )[ ]{ }-_=+\|/?.,<>~`'
t="P@$sword"
attempt=''.join(random.choice(possible)for i in range(len(t)))
attemptNext=''
completed=False
iteration=0

while completed==False:
    print(attempt)

    attemptNext=''
    completed=True

    for i in range(len(t)):
        if attempt[i]!=t[i]:
            completed=False
            attemptNext+=random.choice(possible)
        else:
            attemptNext+=t[i]
    
    iteration+=1
    attempt=attemptNext
    time.sleep(0.1)

print("Target matched after "+str(iteration)+" iterations")