# coding= utf-8
import os
import logging
import calendar
import os
print(os.name)
"""
StringIO
作用：数据的读写不一定是文件，也可以是内存中读写，作用是在内存中读写字符串
ByteIO
作用：stringio他只能操作字符串，bytesio可以操作二进制，作用是在内存中读写二进制
"""
from io import StringIO
from io import BytesIO
# 写/可以写多次/获取写入的内容
fp = StringIO()
fp.write("tony")
fp.write("is")
fp.write("good")
fp.getvalue()
# 读数据
fp = StringIO("good\nnice")
fp.read()


with open("test.txt", "wb") as file1:
    info = "tony is good man"
    info = info.encode("utf-8")
    file1.write(info)
    file1.flush()

with open("test.txt", "r", encoding="utf-8") as file2:
    i1 = file2.read()
    print(file2)
    print(i1)



print(calendar.calendar(2020))
# 日志的生成
logging.basicConfig(level=logging.INFO,
                    filename="./log.txt",
                    filemode="a",
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s")
logging.info("this is good man")
path = r"C:\Users\xiaov\Desktop\测试文档数据‘\连接.txt"
with open(path, "r") as file:
    print(file.read())