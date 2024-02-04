import time 
import threading 

start = time.perf_counter()

def sleep_for_one_sec(seconds) :
    print(f"sleep for {seconds} seconds !")
    time.sleep(seconds)
    print("I'm done sleeping !")
    


list_threads = []
### create 20 threads 
for  _ in range(50) :
    t = threading.Thread(target=sleep_for_one_sec,args=[2])
    t.start()
    list_threads.append(t)
    
### join the threads together 

for thread in list_threads :
    thread.join()
    
finish = time.perf_counter()

print(f"the program finished in : {round(finish-start,2)} seconds")
