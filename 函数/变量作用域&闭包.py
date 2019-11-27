# coding= utf-8
# num = 1
# print(id(num))
# print(num)
#
#
# def func():
#
#     global num
#     num = 30
#     print(num)
#
# func()
# print(num)
#
# # 修改嵌套作用域中的变量
def aa():
    a = 10
    def qq():
        nonlocal a   # 必须嵌套里面有a，
        # 如果没有回报错。如果是全局也报错
        a = 2000
        print(a)
    qq()
    print(a)
aa()

#  闭包
# a = 10
# def func1():
#     b = 20
#
#     def func2():
#         # nonlocal b
#         # b = x
#         c = 30
#         return b
#     return func2
# f2 = func1()
# print(f2())