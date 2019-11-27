# coding= utf-8
# 1, 1,2,3,5,8......

# list1 = [1,2,3,4,5,6,7]
# it = iter(list1)
# print(it)
# 使用函数实现
# def fei(count):
#     index = 0
#     x, y = 0, 1
#     while index < count:
#         print(y)
#         x, y = y, x + y
#         index += 1
#
# fei(5)
# 使用 yiled实现
#
# def fei(count):
#     index = 0
#     x, y = 0, 1
#     while index < count:
#         yield y
#         x, y = y, x + y
#         index += 1
#     return "111111"
#
# g = fei(5)
# for i in g:
#     print(i)
# for循环变量generator 时，拿不到generator的return的返回值
# 如果想拿到返回值，必须捕获stopinterion错误，返回值包含在错误对象的value属性中
def fei(count):
    index = 0
    x, y = 0, 1
    while index < count:
        yield y
        x, y = y, x + y
        index += 1
    return "111111"

g = fei(5)
while True:
    try:
        rest = next(g)
        print(rest)
    except Exception as error:
        print("返回值%s" % error)
        break