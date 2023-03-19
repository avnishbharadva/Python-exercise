import threading
import time 

global x
x = 0

def increment():
    global x
    x += 1

def thread_task():
    for _ in range(100000):
        
        # lock.acquire()
        increment()
        # lock.release()

def main_task():
    global x
    x = 0

    # lock = threading.Lock()
    # t1 = threading.Thread(target=thread_task,args=(lock,))
    # t2 = threading.Thread(target=thread_task,args=(lock,))  # 0.490
    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)  # 0.255

    t1.start()
    t2.start()
    t1.join()
    t2.join()

t = time.time()

for i in range(10):
    main_task()
    print("Iteration {0} : x = {1}".format(i,x))

print("Total Time : ", time.time() - t)