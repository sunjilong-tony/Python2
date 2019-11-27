# coding= utf-8
class aaa(object):
    def __init__(self, age):
        self.age = age

    def __add__(self, other):
        return self.age + other.age

per1 = aaa(12)
per2 = aaa(14)
print(per1 + per2)