# coding= utf-8
import time
a = time.time()
b = time.localtime()
c = time.strftime("%Y-%m-%d %X")
print(a, b, c, end="我们")
DD= time.asctime(b)
z = time.ctime(a)
print(DD)
print(z)
time.sleep(2)
print("hello,tony",end="")
print(1234)
