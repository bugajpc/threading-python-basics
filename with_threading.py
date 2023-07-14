import time
from threading import Thread
def do_this():
    print("Starting this")
    #some code here
    time.sleep(2)
    print("Did this!")

def do_that():
    print("Starting that")
    #some code here
    time.sleep(3)
    print("Did that!")

#do_this()
#do_that()

t1 = Thread(target=do_this)
t2 = Thread(target=do_that)
t1.start()
t2.start()
t1.join()
t2.join()