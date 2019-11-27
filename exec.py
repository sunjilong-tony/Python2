# coding= utf-8
# def func():
#     print("qwer")
#     print("asdf")
#     yield 3
# res = func()
# print(res)
# print(type(res))
# next(res)
# next(res)
# next(res)
# next(res)

import re

print(re.__file__)
#
#
# def phone_set():
#     phone_re = re.compile("^1((3[\d]|(4[1|2])|5[\d]|6[1|2]|7[7|8]|88|9[8|9]\d{8}$))")
#     phone = input("请输入手机号:")
#     if len(phone) != 11:
#         error1 =Exception("手机号必须11位")
#         raise error1
#     elif not isinstance(phone, int):
#         error2 = Exception("必须是数字")
#         raise error2
#     ph = phone_re.search(phone)
#     return ph
#
# try:
#     phone_set()
# except Exception as err:
#     print("%s" % err)
# else:
#     print("执行成功")




# import smtplib
# mstpserver = "smtp.qq.com"
# sender = "aasun.1110@163.com"
# password ="123456"
# meg = ""
# server = smtplib.SMTP(mstpserver, 25)
# server.login(sender,password)
# server.sendmail(sender,[aasun.110@163.com],meg.as_str())
# server.quit()

"""
try:
    pass
except Exception as error:
    print(%error)
else：
    print("正确执行")
finally：
    print（成功）
"""


# # 私有属性使用@property 方法
# def single(cls):
#     instance = {}
#     def inner(*args, **kwargs):
#         if cls not in instance:
#             instance[cls] = cls(*args, **kwargs)
#         return instance[cls]
#     return inner
# # @single
# from enum import  unique
# class Enum:
#     FEB = 0
#     Sun = 1
# print(Enum.Sun)
# class wo:
#     def uo(self):
#         print("ergfv")
#     def __add__(self, other):
#         pass
# class My(object):
#
#     # instance = None
#     # # __slots__ = "sole"
#     # def __new__(cls, *args, **kwargs):
#     #     if cls.instance is None:
#     #         cls.instance = super().__new__(cls)
#     #     return cls.instance
#
#     def __init__(self, name, sole):
#         self.name = name
#         self.age = None
#         self.__sole = sole
#
#     def __setattr__(self, key, value):
#         if key=="age" and value < 0:
#             self.__dict__[key] =0
#         else:
#             self.__dict__[key] =value
#     # def __str__(self):
#     #     return "%s %d" % (self.name, self.__sole)
#
#
#     # @property
#     # def set_sole(self):
#     #     return self.__sole
#     # @set_sole.setter
#     # def set_sole(self, value):
#     #     if not isinstance(value, int):
#     #         raise ValueError("must be integer")
#     #     self.__sole = value
#     def say(self):
#         print("hahahaha")
#
# def mixin():
#     pass
#
# i = My("tony", 10)
# # print(i)
# # print(i.__class__)
# print(i.__dict__)
# class Sun(My):
#     def __init__(self, name, sale, others):
#         My.__init__(self,name,sale)
#         self.others = others
#     def say(self):
#         print("23435")
#
# print(Sun.__bases__)
# print(My.__bases__)
# # print(My.__bases__)
# i.set_sole =1000
# i.money= 100
# def hello(self):
#     print("hello world")
#
# from types import MethodType
# i.hello = MethodType(hello, i)
# i.hello()
# i.set_sole()

"""
栈
先进后出
列表
先进先出
使用类实例化对象
class An(object):
    def func();
    pass
an = An()
an.func()
访问对象的方法
"""
#
#
# def wrapper(cls):
#     instance = {}
#     def inner(*args, **kwargs):
#         if cls not in instance:
#             instance[cls]= cls(*args, **kwargs)
#         return instance[cls]
#     return inner
#
#
# @wrapper
# class Ba(object):
#     # 类属性
#     __solts__ = "name"
#     # instance = None
#     #
#     # def __new__(cls, *args, **kwargs):
#     #     if cls.instance is None:
#     #         cls.instance = super().__new__(cls)
#     #     return cls.instance
#
#     def __init__(self, name, sale):
#         self.name = name
#         self.__sale = sale
#         self.age = None
#
#     @property
#     def set_sale(self):
#         return self.__sale
#
#     @set_sale.setter
#     def set_sale(self, value):
#         if not isinstance(value, int):
#             raise ValueError("must be int")
#         self.__sale = value
#
#
#     def say(self,name):
#         print("hello world %s" % self.name)
#     def __del__(self):
#         pass
#     # 类方法
#     @classmethod
#     def an(cls):
#         pass
#     # 静态方法
#     @staticmethod
#     def ab():
#         pass
# ba = Ba("tony", 18)
# ba.say("tony")
# ba.age = 19
# print(ba.age)
# ba.qq = 123456
# print(ba.qq)
# def zz(self):
#     print("zz")
# from types import MethodType
# ba.zz = MethodType(zz, ba)
# ba.zz()
# s = Ba("na", 40)
# print(s)
# # 单例实现
# """
# 1使用模块实现
# 2使用new实现
# 3.使用装饰器实现
# """
# 2
#
#
#

import base64
# ll = b"i am happy"
# print(base64.b64encode(ll))
# uu = b'aSBhbSBoYXBweQ=='
# print(base64.b64decode(uu))
# import hashlib
# user = b"tony sun"
# ha= hashlib.md5()
# ha.update(user)
# print(ha.hexdigest())
# passed =  b"tony sun"
# md5 = hashlib.sha1()
# md5.update(passed)
# import hmac
# key =b"wpm"
# H = hmac.new(key,passed,digestmod = "SHA1")
# print(H.hexdigest())
# import uuid
# name = "tony"
# namespace = uuid.NAMESPACE_URL
# print(uuid.uuid1())
# print(uuid.uuid3(namespace, name))
# import os
# print(os.name)
# print(os.listdir("./"))
# # print(os.environ)
# """
# os.rename()
# os.remove()
# os.system()
# os.mkdir()
# os.rmdir()
# os.getcwd()
# os.path.spilt()
# os.path.join()
# os.path.getsize()
# os.path.isdir()
# os.path.isfile()
# """
# import functools
#
# int2 = functools.partial(int, base = 2)
# ab ="0100"
# print(int2(ab))
# import collections
# op = collections.deque()
# # op 相当于列表 同时是双向的取值
# dd = {}
# dd = collections.defaultdict(lambda :"没有此值")
# print(dd["name"])
# p = collections.namedtuple("point", ["x", "y"])
# p(1,2)
# print(p)
# """
# dict
# dict = {}创建一个而空字典
# dict[1]= 1赋值
# del dict[1] 删除键值
# dict.pop(""， "提示) 删除键值，同时返回提示
# """
# collections.OrderedDict()
# import pygame
# pygame.init()
# pygame.quit()
# import sys
# print(sys.path)
# # # sys.argv()
# # sys.stdin.readline()
# sys.stdout.write("hello"+"\n")
# print("*" * 50)
# import time
# t  = time.time()
# print(time.time())
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %X"))
# print(time.ctime(t))
# time.sleep(2)
# # print("ha ")
# # time.clock()
# # time.sleep(4)
# # print(time.clock())
# import datetime
# print("-------------")
# bi = datetime.datetime.now()
# print(bi)
#
# # import calendar
# # print(calendar.calendar(12))
# from PIL import Image, ImageDraw, ImageFont, ImageFilter
# import random
# def red():
#     return chr(random.randint(60, 100))
# # 随机颜色1:
# def rndColor():
#     return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)
# # 随机颜色2:
#
# def rndColor2():
#     return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)
#
# im = Image.new("RGB", (240, 60), (255, 255, 255))
# font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", 50)
# # 含义：创建一个可以在给定图像上绘图的对象。
# draw = ImageDraw.Draw(im)
# for x in range(100):
#     for y in range(20):
#         draw.point((x, y), fill=rndColor())
#
# for t in range(4):
#     draw.text((60 * t + 10, 10), red(), font=font, fill=rndColor2())
# im = im.filter(ImageFilter.BLUR)
# im.save('code.jpg', 'jpeg')
#
# import calendar
#
# print(calendar.calendar(2017))
# import json
# dd = {"name": "tony", "age": 18}
# dd_json = json.dumps(dd)
# print(dd_json)
# print(type(dd_json))
# dd_pyton = json.loads(dd_json)
# print(dd_pyton)
# print(type(dd_pyton))
# import itertools

# """
# 可迭代对象
# 列表的生成式
# 可以叠加
# 使用isinstance查询
#
# 生成器
# 将列表生成式换成（），
# 函数将return换成yield
# 迭代器
# iter（）
#
#
# 使用next取值
# """
# # 函数的定义：封装一些功能，方便后续的使用
# #简单的函数
# def asdf():
#     pass
# # 函数的返回值
# def qq():
#     return
# # 传递函数
# def aa(a):
#     return a
# # 关键之参数
# import keyword
# print(keyword.kwlist)
# """
# ['False', 'None', 'True', 'and', 'as', 'assert',
#  'break', 'class', 'continue', 'def', 'del', 'elif',
#  'else', 'except', 'finally', 'for', 'from', 'global',
#  'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
#  'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#  """
# # 多个返回值
# def ww(*args, **kwargs):
#     return args, kwargs
# # 函数也是一种数据即是可以数据作为参数传递
# """
# 闭包
# 内函数调用外函数的参数，并返回
# """
# def a():
#     b = 0
#     def c():
#         nonlocal b
#         b = 100
#         return b
#     return c
# """
# 装饰器
# 是一个闭包，将函数作为参数进行传递，并返回函数的引用
# """
# def pp(f):
#     def nn():
#         f()
#     return nn
# # 匿名函数
# li = lambda x, y: x + y
# print(li(1, 2))
# """
# map
# 将函数作用在lsd上，并飞回一个iterator
# reduce
# 将函数作用在lsd上，返回的返回值和下一个元素结合返回，直到和lsd接完完成
# 需要2个参数
# fiter
# 将函数作用在lsd上，根据返回的值判断是要
# sorted
# 排序
# evel
# 字符串的计算
# """

# dd = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# aa = dd.items()
# ll = []
# for i in aa:
#     ll.append(i)
# print(ll)
# bb = OrderedDict(ll)
# cc = OrderedDict(dd)

# print(cc)

# for i, k in dd.items():
#     print(k)

# c=datetime.datetime.now()
# print(c)
# # b = calendar.calendar(2017)
# print(b)

# li = [i for i in range(8)]
# print(li)
# x = 1
# y =2
# a =lambda x, y: x+y
# print(a(1,6))
# def func():
#     yield 0
#     print("11111111")
#     yield  1
#     print("222222222222")
#     yield 3
# res = func()
# print(res)
# print(type(res))
# print(next(res))


# a = time.time()
# print(a)
# b = time.localtime()
# print(b)
# c = time.strftime("%Y-%m-%d %X")
# print(c)
# print(time.asctime(b))
# print(time.ctime(a))




# """
# 我們很開心
# """
#
# def hello():
#     """注釋"""
#     print("hahahha")
# hello()
# #
# #


# str_1 = "更改了\t某人\t \n 信息\t"
# #print(str_1)
# str_list = str_1.split("人")
# print(str_list)
# str_2=",\n".join(str_list)
# #print(str_2)
# var = 10                    # 第二个实例
# # while var > 0:
#     var = var -1
#     if var == 5:             # 变量为 5 时跳过输出
#         break
#     print('当前变量值 :', var)
# print("Good bye!")


# def test(num):
#     print("在函数%d对应的内存地址为%d" % (num, id(num)))
#     result = "hello"
#     print("函数返回的内存地址为%d" % id(result))
#     return result
# a = 1
# print("a这个id的地址是%d" %id(a))
# r = test(a)
# print("%s 的内存地址是%d" % (r, id(r)))


# def normalize(L1):
#     return str(L1).capitalize()
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)
# from functools import reduce
#
# # DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# #
# # def str2int(s):
# #     def fn(x, y):
# #         return x * 10 + y
# #     def char2num(s):
# #         return DIGITS[s]
# #     return reduce(fn, map(char2num, s))
#
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
# def char2num(s):
#     return DIGITS[s]
#
# char2num("123")

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())