# coding= utf-8
class a(object):
    def __init__(self, x):
        self.x = x

    def aa(self):
        print("%s" % self.x)


class b(object):
    def __init__(self, y):
        self.y = y

    def bb(self):
        print("%s " % self.y)
        
class c(a,b):
    def __init__(self, x, y):
        a.__init__(self, x)
        b.__init__(self, y)

    def cc(self):
        print("%s %s" % (self.x, self.y))
#
# aa= a("1")
# aa.aa()
# bb = b("2")
# bb.bb()
cc = c("4", "5")
print(cc)
cc.cc()



