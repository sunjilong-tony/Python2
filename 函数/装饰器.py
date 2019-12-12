# coding= utf-8


# def outer(fun1):
#     def inner(age):
#         if age < 0:
#             age = 0
#         fun1(age)
#     return inner
# # # say = outer(say)
# @outer # 相当于say = outer(say)
# def say(age):
#     print("%d" % age)
# say(-10)

# 通用的装饰器
# def outer1(fun1):
#     def inner(*args, **kwargs):
#         #添加修改的功能
#         print("********")
#         fun1(*args, **kwargs)
            # 如果要修改原函数的返回值，在这修改
# #     return inner
# # 修改内容
# def outer1(fun1):
#     def inner(*args, **kwargs):
#         #添加修改的功能
#         print("********")
#         if args <= 0:
#             args = 0
#         fun1(*args, **kwargs)
#     return inner
# @outer1 #函数的参数理论上是无限制的，但最好不要超过6个
# def say1(age, name):
#     print("%d %s" % (age, name))
# say1(-10, "tony")
#
def decorator_a(func):
    print('Get in decorator_a')

    def inner_a(*args, **kwargs):
        print('Get in inner_a')
        return func(*args, **kwargs)
    return inner_a


def decorator_b(func):
    print('Get in decorator_b')

    def inner_b(*args, **kwargs):
        print('Get in inner_b')
        return func(*args, **kwargs)
    print("bbbbbbbbbb")
    return inner_b


@decorator_a
@decorator_b
def f(x):
    print('Get in f')
    return x * 2


f(20)

# import time
# def retry(count, wait=0):
#     def wrapper(f):
#         def inner(*args, **kwargs):
#             for i in range(count):
#                 try:
#                     f(*args, **kwargs)
#                 except Exception as error:
#                     time.sleep(wait)
#                     continue
#                 else:
#                     return f
#         return inner
#     return wrapper
#
#
# def decorator(count,wait=0):
#     def wapper(f):
#        pass
#     return wapper
