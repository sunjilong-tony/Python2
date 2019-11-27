# coding= utf-8
import time


def retry(count, wait=0):
    def wrapper(f):
        def inner(*args, **kwargs):
            for i in range(count):
                try:
                    res = f(*args, **kwargs)
                except Exception as error:
                    time.sleep(wait)
                    continue
                else:
                    return res
        return inner
    return wrapper


@retry(5)
def connectSQL(ip,port,dbname,passwd):
    pass
