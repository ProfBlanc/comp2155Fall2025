import threading
import time

#  define a function
def print_numbers(start, end):
    for i in range(start, end+1):
        print(f"#{i}")
        time.sleep(1)


# create a thread and refer to a function
t1 = threading.Thread(target=print_numbers,
                      args=(1, 5))

# start/new     run     wait, timed-wait, blocked   terminated/dead

# start the thread
t1.start()
# t1.join()
print(threading.current_thread().name + " has finished.")

