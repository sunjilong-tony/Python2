# coding= utf-8
import collections
from collections import namedtuple

# deque = collections.deque()
# print(deque)
p = (1,2)
# 定义一个新的数据类型，属于tuple类型的子类型
point = namedtuple("point", ["x","y"])
point = (1,2)

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict)
aaa = dict.items()
print(aaa)
dict = collections.OrderedDict([('Age', 7), ('Name', 'Zara'), ('Class', 'First')])
print(dict)
print(dict)
print(dict)
print(dict)
dict["aa"] = "lsdlf"
print(dict)