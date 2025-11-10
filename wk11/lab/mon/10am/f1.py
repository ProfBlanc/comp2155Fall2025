def counting(title, num_from, num_to):
    print("Starting Counter named", title)

    start = num_from
    end = num_to
    step = 1
    if num_from > num_to:
        start = num_to
        end = num_from

    for num in range(start, end + step, step):
        print(title, num)

counting("First", 1, 10)
counting("Second", 20, 10)

print("*" * 10)
import threading

#t1 = threading.Thread(target=counting, args=("Third", 15, 25000))
#t2 = threading.Thread(target=counting, args=("Fourth", 100, 90000))
t1 = threading.Thread(target=counting, args=("Third", 15, 25))
t2 = threading.Thread(target=counting, args=("Fourth", 100, 90))

# print("hi" + 123)

t1.start()
print("hi" + 123)
t2.start()

