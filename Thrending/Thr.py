from threading import *
from time import sleep
class HELLO(Thread):
    def run(self):
        for i in range(500):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(500):
            print("Hi")
            sleep(1)

t1= HELLO()
t2 =Hi()

t1.start()
sleep(0.2)
t2.start()

#Join All Threads
t1.join()
t2.join()

print("SAJITH ")
