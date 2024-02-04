# when we use threading. So we're going to run this function, and we can see that it comes up here and waits 
# a second. But as soon as that starts waiting, our code is just going to move on and go ahead and run another 
# function while we're waiting for this one second to be done sleeping. And then we kick off this other second. 
# So these are actually overlapped here, but we never actually ran any of this code at the same time, it's just 
# going to give the illusion of running the code at the same time. And then finally, we can see that we are done 
# a little bit sooner.

###### THIS SCRIPT IS BEING EXECUTED SYNCHRONOUSLY 
###### it isn't doing so much on the cpu and just waiting like this 
###### that's usually a good sign of when we can use some benefits of threading and concurrency 

import threading 
import time 

start = time.perf_counter()


def sleeping() :
    print("I'm gonna sleep for 1 second")
    time.sleep(1)
    print("I'm done sleeping !")
    

t1 = threading.Thread(target=sleeping)
t2 = threading.Thread(target=sleeping)

t1.start()
t2.start()

t1.join()
t2.join()


finish =time.perf_counter()

print(f"The script has finished in : {round(finish-start)} seconds :)")
    