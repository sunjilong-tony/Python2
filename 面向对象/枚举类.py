# coding= utf-8
from enum import Enum, unique
# month = Enum("Month", ("Jan", "Feb", "Mar"))
# n = month.__members__.items()
# print(type(n))
# print(n)
# for name, member in n:
#     # value 属性是自动赋值默认从1开始
#     print(name, member, member.value)

# 自定义枚举类，这样可恶意更精确的设置值
# 装饰器检查并保存没有重复变量
@unique
class Month(Enum):
    Jan = 0
    Feb = 1
    Mar = 2
print(Month.Jan.value)


