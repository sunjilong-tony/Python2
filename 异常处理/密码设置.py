# coding= utf-8
import os
from os.path import  *


def set_password():
    pwd = input("请输入密码： ")
    if len(pwd) < 8:
        er = Exception("密码要大于8位")
        raise er
    return pwd

try:
    set_password()
except Exception as error:
    print("未知错误：%s" % error)

else:
    print("设置成功")
finally:
    print("结束")

print(os.__name__)

