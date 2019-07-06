# problem with Lock()
# The standard Lock does not know which thread is currently holding the
# lock. If the lock is held, any thread that attempts to acquire it will
# block, even if the same thread itself is already holding the lock.


from threading import Thread,Lock
import threading
import time

l = Lock()

def task():
    for i in range(1,11):
        l.acquire() # dont remember to which thread it has given lock
        '''
            any thread try to execute below line will be blocked
            even for the same thread which acquired lock
            so to avoid this used RLock() (re entrant lock)
        '''
        l.acquire()
        time.sleep(1)
        print('inside lock',threading.current_thread().name)

        l.release()#release lock, allow other thread to take over



t1 = Thread(target=task)
t2 = Thread(target=task)
t1.start()
t2.start()