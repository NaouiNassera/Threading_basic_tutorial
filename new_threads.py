import time 
import concurrent.futures 

start = time.perf_counter()

def sleep_a_bit(sec) :
    print(f"i'm sleeping for {sec} seconds !")
    time.sleep(sec)
    return f"slept for {sec} seconds & I'm done :p"

# duration to sleep 

sec_to_sleep = [5,4,3,2,1]
with concurrent.futures.ThreadPoolExecutor() as executor :
    results = executor.map(sleep_a_bit,sec_to_sleep)
    for result in results :
        print(result)
        
        
        
finish = time.perf_counter()

print(f"Program being executed for {round(finish-start,2)} seconds !")