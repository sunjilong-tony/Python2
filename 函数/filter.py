# coding= utf-8

li1 = [1,2,3,4,5,6,7,8]
def fun( num):
    if num % 2 == 0:
        return True
    return False

ll = filter(fun, li1)
print(list(ll))

# 删除列表中是空字符串的元素
li2 = ["a", "b", "", " "]
def f(item):
    return item and item.strip()


aa = filter(f, li2)
print(list(aa))
