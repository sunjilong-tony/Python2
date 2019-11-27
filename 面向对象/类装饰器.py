# coding= utf-8
class A():
    pass
def func():
    pass

a = A()
print(func.__call__)
print(A.__call__)
class Addxing(object):
    def __init__(self, f):
        self.f = f
    def __call__(self, *args, **kwargs):
        print("11111111")
        res = self.f()
        return res


@Addxing



def f():
    print("******************")

f()
"""" obj = Addxing(func)
func= obj()
func()   obj.__call__()
"""