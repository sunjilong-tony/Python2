# coding= utf-8


class Person(object):
    def __init__(self, name):
        self.name = name

    def feed_animal(self, ani):
        ani.eat()
