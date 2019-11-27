# coding= utf-8
import time


def timer(f):
    def inner(*args, **kwargs):
        time1 = time.time()
        res = f()
        time2 = time.time()
        print("运行时间%.2f" % (time2 - time1))
    return inner

@timer
def aa():
    print("1111")
    time.sleep(2)
    print("22")

aa()

