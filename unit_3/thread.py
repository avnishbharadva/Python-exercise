import threading
import time

def myprint(n):
    for i in range(1,n):
        print(i)
        time.sleep(0.5)

print("Start")

t1 = threading.Thread(target=myprint,args=(6,))
t2 = threading.Thread(target=myprint,args=(6,))

t1.start()
t1.join()

t2.start()
t2.join()

print("End")