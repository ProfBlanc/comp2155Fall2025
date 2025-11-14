"""
change the value of a shared resourse using threads

"""
import threading, random, time
shared_object = "bottle"

def move(person, replaced_object):
    global shared_object

    pause_time = random.randint(5, 25) * 0.1

    previous_object_value = shared_object
    print(f"({person}) current value is {shared_object}")
    print(f"{person} wants to replace {shared_object} to {replaced_object}")
    time.sleep(pause_time)
    shared_object = replaced_object

    print(f"{person} successfully replaced {previous_object_value} to {shared_object}")


t1 = threading.Thread(target=move, args=("John", "phone"))
t2 = threading.Thread(target=move, args=("Mary", "desk"))
t3 = threading.Thread(target=move, args=("Jen", "screen"))

threads = [t1, t2, t3]

for t in threads:
    t.start()