# coding= utf-8
import uuid
import base64
import hashlib
import hmac
import itertools
import time
#itertools.product(iterable,repeat=1)
passwd = ["".join(i) for i in itertools.product("12345678",repeat=2)]
print(passwd)
#itertools.combinations(iterable,length)
# o = list(itertools.combinations([1,2,3,4],3))
# print(o)
#itertools.permutations(iterable,length)
#从n个不同的元素中取出m（m<n）个元素，按照一定的顺序
# 排成一列，叫做从n个元素中获取m个元素的一个排列，
# 如果m=n，这个排列叫全排列
# p = list(itertools.permutations([1,2,3,4],2))
# cha = itertools.chain("ABC", "abc")
# for i in cha:
#     print(i)
# g = itertools.groupby("aaaasvdvgrga")
# for i ,k in g:
#     print(i ,list(k))
# c = itertools.count(1)
# for i in c:
#     print(i)
#     time.sleep(1)
# s = "womenhenxihuan"
# s= s.encode("utf-8")
# key = b"123456"
# h = hmac.new(key,s,digestmod="MD5")
# print(h.hexdigest())
# # qq = "i am happy"
# qq_encode = qq.encode("utf-8")
# md5 = hashlib.md5()
# md5.update(qq_encode)
# print(md5.hexdigest())

name = 'test_name'
namespace = 'test_namespace'
# namespace = uuid.NAMESPACE_URL

print(uuid.uuid1())
print(uuid.uuid3(namespace, name))
print(uuid.uuid3(namespace, name))
print(uuid.uuid4())
print(uuid.uuid5(namespace,name))
#
# s = "i am tonydf"
# b = 'aSBhbSB0b255ZGY='
# print(base64.b64encode(s.encode("utf-8")))
# print(base64.b64decode(b))