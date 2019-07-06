from threading import Thread,Lock
import threading
import time

l = Lock()

def task():
    for i in range(1,11):
        l.acquire()# only one thread(with lock) can access below code at a time
        time.sleep(1)
        print('inside lock',threading.current_thread().name)
        l.release()#release lock, allow other thread to take over



t1 = Thread(target=task)
t2 = Thread(target=task)
t1.start()
t2.start()