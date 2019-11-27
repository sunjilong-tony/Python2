# coding= utf-8
"""
作用：用来对一个函数一个类或者一个模块进行正确检测的检测工具
结果：
1.单元测试通过 说明测试的函数或者类能够正常工作
2.单元测试fail 要么有bug，要么测试的条件输入不正确
意义：
1.假设对函数的代码进行了修改，只需在跑一次单元测试，如果通过，说明此时的修改不会对
函数的原有行为赵成影响

"""

# 原有函数
def my(x,y):
    ret= x+ y
    return ret

ret =my(1,2)
print(ret)

#修给函数 +1
#导入uuittest,创建的类要继承这个属性
import unittest
class Test(unittest.TestCase):
    def setUp(self):
        print("start ")
    def tearDown(self):
        print("gover")
        # 测试函数名 test__待测函数名
        def test__my(self):
            self.assertEqual(my(1,2),3)

if __name__ == '__main__':
    unittest.main()

class Mydict(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __setattr__(self, key, value):
        pass

