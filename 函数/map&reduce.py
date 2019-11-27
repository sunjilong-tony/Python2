# coding= utf-8
def char2int(chr):
    return {"0": 0, "1": 1, "2": 2, "3": 3}[chr]
ret = map(char2int, "123")
print(ret)
print(list(ret))
# from functools import reduce
# # def func(x, y):
# #     return x + y
# # res = reduce(func, [1, 2, 3, 4, 5])
# # print(res)
# def str2int(s):
#     def char2int(chr):
#         return {"0": 0, "1": 1, "2": 2, "3": 3}[chr]
#     def f(x, y):
#         return x * 10 + y
#     return reduce(f, map(char2int, s))
# res = str2int("123")
# print(res)
