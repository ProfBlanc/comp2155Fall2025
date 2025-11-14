"""
threads aka workers
    process/running tasks at the same time


"""
import threading
import time

def print_numbers(title, num):
    for i in range(1, num + 1):
        print(f"{title} task #{i}")
        time.sleep(1)

# print_numbers("first", 5)
# print_numbers("second", 5)

t1 = threading.Thread(target=print_numbers, args=("first", 50))
t2 = threading.Thread(target=print_numbers, args=("second", 50))

"""
    new/ready
    run
        waiting, time-waiting, block
    terminated/dead
"""

t1.start()
t2.start()
