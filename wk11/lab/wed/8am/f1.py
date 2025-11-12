import threading
import time

shared_value = True

def print_numbers(start, end):
    global shared_value
    for i in range(start, end+1):
        print(f"#{i}")
        if i == round(end/2): shared_value = False
        if not shared_value:
            print("Interrupted")
            shared_value = True
        time.sleep(1)

t1 = threading.Thread(
    target=print_numbers,
    args=(1, 5)
)
# born/new    run     wait,timed wait, blocked    terminated/dead

t1.start()
t1.join()  # wait for above threads to finish before running statement below
print("End of thread " + threading.current_thread().name)

