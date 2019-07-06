# Semaphores are simply advanced counters.
# An acquire() call to a semaphore will block only after a number of threads
# have acquire()ed it.
# The associated counter decreases per acquire() call,
# and increases per release() call.

from threading import Thread,BoundedSemaphore
import threading
import time


b = BoundedSemaphore(3) # only three threads are allowed
# once after three threads completes their execution, fourth thread will be allowed

def task():
    b.acquire()
    for i in range(1,11):
        time.sleep(0.5)
        print(i,threading.current_thread().name)
    b.release()

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)
t3 = threading.Thread(target=task)
t4 = threading.Thread(target=task)
t1.start()
t2.start()
t3.start()
t4.start()