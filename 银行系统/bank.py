# coding= utf-8
from singledemo import singledemo

@singledemo
class Bank(object):
    def __init__(self):
        self.userDict = {}