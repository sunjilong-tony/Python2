# coding= utf-8
import time

time.clock()
sum = 0
for i in range(10000000):
    sum += i

print("%d " % time.clock())