import threading
import time

def thread_fn_1(my_val):
    for i in range(10):
        print(i, my_val)
        time.sleep(1)

def other_code():
    for i in range(10):
        print(i, "other code!")
        time.sleep(1)

if __name__ == '__main__':
    print("Starting")

    thread1 = threading.Thread(target=thread_fn_1, args=(1,))
    thread1.start()

    thread2 = threading.Thread(target=thread_fn_1, args=(2,))
    thread2.start()

    other_code()



