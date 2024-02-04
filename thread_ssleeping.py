###### THIS SCRIPT IS BEING EXECUTED SYNCHRONOUSLY 
###### it isn't doing so much on the cpu and just waiting like this 
###### that's usually a good sign of when we can use some benefits of threading and concurrency 


import time 

start = time.perf_counter()


def sleeping() :
    print("I'm gonna sleep for 1 second")
    time.sleep(1)
    print("I'm done sleeping !")
    

sleeping()
sleeping()
sleeping()
sleeping()
sleeping()

finish =time.perf_counter()

print(f"The script has finished in : {round(finish-start)} seconds :)")
    