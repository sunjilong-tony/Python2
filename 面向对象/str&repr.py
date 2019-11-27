# coding= utf-8
class Person(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return ("11111111%s" % self.name)

    def __repr__(self):
        return ("2222 %s" % self.name)

    def say(self):
        print("%s" % self.name)
per1 = Person("qwe")
per1