#in python 3.2 they added the thread pool executor 

# They added something called a thread pool executor and in a lot of cases This is going to be an easier and 
# more efficient way to run these threads.

#And it also allows us to easily switch over to using multiple processes instead of threads as well, depending 
# on the problem that we're trying to solve
import time 
import concurrent.futures
 
# start time of the script 
start = time.perf_counter()

 
# the function 
def sleeping() : 
    print("sleeping for one second")
    time.sleep(1)
    return "done sleeping"



# And when we use this thread pool executor, it's usually best to use this with a context manager.
""""
#### to run just one thread 
with concurrent.futures.ThreadPoolExecutor() as executor :
    th = executor.submit(sleeping)
    print(th.result())
"""

## to run two threads for example 
""""
with concurrent.futures.ThreadPoolExecutor() as executor : 
    f1 = executor.submit(sleeping)
    f2 = executor.submit(sleeping)

    print(f1.result())
    print(f2.result())
    
"""

### the function sleep_time 

def sleep_time(seconds) :
    print(f"starting sleeping for {seconds} seconds!")
    time.sleep(seconds)
    return f"done sleeping {seconds}!"

#### to run multiple threads  example 

### we do use use list comprehension to create multiple threads 

sec_to_sleep = [5,4,3,2,1]

with concurrent.futures.ThreadPoolExecutor() as executor :
    threads = [executor.submit(sleep_time , sec) for sec in sec_to_sleep ]
    
    #### THE RUSLTS ARE CAPTURED AS SOON AS WE HAVE THE CREATION OF THREADS WHICH IS DONE 
    for f in concurrent.futures.as_completed(threads) :
        print(f.result())
    
    
finish = time.perf_counter()

print(f"The script has finished in : {round(finish-start)} seconds :)")














