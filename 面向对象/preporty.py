# coding= utf-8
# 做装饰器使用


class Student(object):

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = value
s = Student()
s.score = 60
print(s.score)


# @property把一个函数变成一个静态属性
#  直接调用函数名字，不需要加括号，就能获取到函数返回值。一般用在不注重过程，只要结果的情况!
class Person(object):
    @property
    def func(self):
        return "hello"

per1 = Person()
print(per1.func)
