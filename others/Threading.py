import threading
import time

def tstart(arg):
    time.sleep(0.5)
    print("%s running...." % arg)

if __name__ == '__main__':
    t1 = threading.Thread(target=tstart, args=('This is thread 1',))
    t2 = threading.Thread(target=tstart, args=('This is thread 2',))
    t1.start()
    t2.start()
    print("This is main function")