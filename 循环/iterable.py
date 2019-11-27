# coding= utf-8
from collections import Iterable

print(isinstance([], Iterable))
print(isinstance("tony", Iterable))
print(isinstance(123456, Iterable))
print(isinstance({}, Iterable))
print(isinstance((), Iterable))
print(isinstance(set(), Iterable))
print(isinstance((x for x in range(10)), Iterable))
# 列表生产式
li2 = [x * x for x in range(1, 11)]
print(li2)
# 列表生成式的for 循环可以加判断
li3 = [x * x for x in range(1, 11) if x % 2 == 0]
print(li3)
# 使用双层循环，生成全排列
li4 = [m + n for m in "ABC" for n in "123"]
print(li4)
li4 = []
for i in["Sun", "KAIGE", "Good", "nice"]:
    ii = i.lower()
    li4.append(ii)
print(li4)
lllll = ["Sun", "KAIGE", "Good", "nice"]
liist = [i.lower() for i in lllll]
print(liist)
# 创建生成器
# 修给列表生成式，将列表生成式给成（）
li5 = (x * x for x in range(1, 6))
print(li5)
print(type(li5))
# 特点：可以使用next（）的函数的generator的下一个值,
# 当所有元素拿出来后，会得到StopIteration异常。循环使用for
# print(next(li5))
# print(next(li5))
# print(next(li5))
for i in li5:
    print(i)

# 函数实现生成器（yield）
#推到的算法比较复杂，用列表生成for 循环无无法实现可以使用函数生成器
#函数是按顺序执行，遇到return 语句或最后一行函数语句返回
# 如果想让一个函数变成生成器，只要将函数的return改成yield
# 编程generator函数，在每次调用next（）的时候，遇到yield语句返回，
#如果再次遇到next（），会从上次返回的yield语句继续执行
def func():
    print("qwer")
    print("asdf")
    yield 3
res = func()
print(res)
print(type(res))
next(res)
next(res)

