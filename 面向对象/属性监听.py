# coding= utf-8
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "name: %s age: %d" % (self.name, self.age)

    def run(self):
        print("%s run" % self.name)

    def __getattr__(self, item):
        if item == "weight":
            return 180
        else:
            raise AttributeError

    def __setattr__(self, key, value):
        if key == "age" and value < 0:
            # self.age = 0 不能写self.attr,会在调用__setattr（），会造成死循环
            self.__dict__[key] = 0
        else:
            self.__dict__[key] = value
    # 以后避免实现该方法
    # def __getattribute__(self, item):
    #     print("---------", item)
    #     super().__getattribute__(item)
per = Person("tom", - 20)
print(per.age)
print(per.weight)
"""
__getattr__
拦截点号运算:获取定义的内容，如果没有对应的属性，上抛报错
__setattr__
拦截所有属性的赋值语句,对所有属性的值进行定义
__getattribute__
有和没有都执行
"""
