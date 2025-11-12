import random
import threading
import time

def worker(name, num):

    pause_time = random.randint(75, 150)
    pause_time /= 100

    for i in range(1, num + 1):
        print(f"Worker {name} is working on task {i}")
        time.sleep(pause_time)

# create 3 threads with 3 unique names and numbs b/w 3-5
t1 = threading.Thread(target=worker, args=("John", 4))
t2 = threading.Thread(target=worker, args=("Mary", 5))
t3 = threading.Thread(target=worker, args=("Jen", 3))

# create a list of 3 threads
thread_list = [t1, t2, t3]

# run the threads above
for t in thread_list:
    t.start()
