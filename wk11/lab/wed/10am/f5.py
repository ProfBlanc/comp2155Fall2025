"""
creating a method named move
    name, target_object
        output name and object target object to move
        grab the object
        output name and target object
"""
import random
import threading
import time

shared_object_value = "bottle"
lock = threading.Lock()
def move(name, target_object):
    global shared_object_value
    lock.acquire()
    pause_time = random.randint(75, 250) / 100
    print(f"({name}) The current shared object value is", shared_object_value)
    print(f"{name} wants to replace {shared_object_value} to {target_object}")
    time.sleep(pause_time)
    print(f"{name} has successfully replaced {target_object} to {shared_object_value}")
    shared_object_value = target_object
    lock.release()

t1 = threading.Thread(target=move, args=("John", "desk"))
t2 = threading.Thread(target=move, args=("Mary", "chair"))
t3 = threading.Thread(target=move, args=("Jen", "phone"))

t1.start()
t2.start()
t3.start()