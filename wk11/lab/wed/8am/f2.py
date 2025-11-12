import threading, time

def worker(name, num):
    for i in range(1, num + 1):
        print(f"Worker {name} is working on task {i}")
        time.sleep(1)

# create a list of 3 threads
# each thread calls worker func with unique name and num
# start each of the threads in the list of threads

t1 = threading.Thread(target=worker, args=("John", 4))
t2 = threading.Thread(target=worker, args=("Mary", 3))
t3 = threading.Thread(target=worker, args=("Jennifer", 5))

thread_list = [t1, t2, t3]

for t in thread_list:
    t.start()
