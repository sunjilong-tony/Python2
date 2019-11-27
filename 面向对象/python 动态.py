# coding= utf-8
from types import MethodType


class Demo(object):
    __slots__ = ("name", "age")
    rebulid_new = None
    rebulid_init = False
    # 单例设计
    def __new__(cls, *args, **kwargs):
        if cls.rebulid_new is None:
            cls.rebulid_new = super().__new__(cls)
        return cls.rebulid_new
    # 初始化一次
    def __init__(self, name, age, weight):
        # if cls.rebulid_init is False:
        #     return
        # cls.rebulid_init = True
        self.name = name
        self.age = age
        self.__weight = weight

    def __str__(self):
        return ("%s is %d %d" % (self.name, self.age,self.__weight))
    # 设置属性监听
    def __setattr__(self, key, value):
        if key == "age" and value < 0:
            self.__dict__[key] = 0
        else:
            self.__dict__[key] = value
     # property 将方法设置成一种属性
    # @property
    # def run(self):
    #     return "run"
    # property 将其设置成一个装饰器(对私有属性设置)
    @property
    def weight(self):
        return self._weight
    @weight.setter
    def set_weight(self,value):
        if isinstance(value, int):
            raise ValueError("请输入整数")
        if value >20 or value <100:
            raise ValueError("QIN SHUR ")
        self._weight = value

# 偏函数
import functools
functools.partial(int,base= 2)
# @classmethod
# def fun():
#     pass
# @staticmethod



tony = Demo("tony", -1,100)
# 动态添加属性
print(tony)
# 动态添加方法
def func(self):
    print("func")
tony.func = MethodType(func, tony)
tony.func()

# print(tony.run)



class Demo2(Demo):
    def __init__(self):
        pass
    # 运算符重载
    def __add__(self, other):
        return self.age +other.age

from enum import Enum




class A():
    pass
class B():
    pass



