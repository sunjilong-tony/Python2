# coding= utf-8
class Person(object):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name):
        print("-------------------")
        self.name = name
        self.age = 0

    def say(self):
        print("%s" % self.name, self.age)
per1 = Person("wom")
per1.say()
per1.money = 100
print(per1.money)
# 添加方法


def run(self):
    print("run")
from types import MethodType
per1.run = MethodType(run, per1)
per1.run()