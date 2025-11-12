import random
import threading
import time

object_to_move = "bottle"

def move(person, object):
    global object_to_move
    print(f"The current object value is {object_to_move}")
    print(f"Person {person} wants to move object {object}")
    wait_time = random.randint(75, 150)
    wait_time /= 100

    time.sleep(wait_time)
    object_to_move = object
    print(f"Person {person} has successfully moved object {object_to_move}")

t1 = threading.Thread(target=move, args=("John", "chair"))
t2 = threading.Thread(target=move, args=("Mary", "desk"))
t3 = threading.Thread(target=move, args=("Jen", "phone"))

threads = [t1, t2, t3]
for t in threads:
    t.start()