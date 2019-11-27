# coding= utf-8
# mixin 一般省略object
class fixmixin:
    def fixphone(self):
        print("fix phone")
    def fixcomputer(self):
        print("fix computer")
    def say(self):
        print("6666666666")
class Person(object):
    def __init__(self, name):
        self.name = name
    def say(self):
        print("good man")
class Student(Person):
    def __init__(self, name, stdid):
        super().__init__(name)
        self.stdid = stdid
# 给pyclass动态添加父类pymixinclass
# flag =1,则将pymixincalss设置为主要父类
# 在Python中，每一个类有一个__bases__属性，列出其基类
def mixin(pyClass, pyMixinClass,flag=0):
    if flag:
        pyClass.__bases__ = (pyMixinClass,) + pyClass.__bases__
    elif pyMixinClass not in pyClass.__bases__:
        pyClass.__bases__ += (pyMixinClass,)


mixin(Student, fixmixin, 1)
stu = Student("tom", 123456)
print(Student.__mro__)
print(Student.__bases__)
# print(stu.__class__)
print(stu.__dict__)
# stu.say()