# coding= utf-8
class MyLove(object):
    add = None
    init_flag = None

    def __new__(cls, *args, **kwargs):
        if cls.add is None:
            cls.add = super().__new__(cls)
        return cls.add

    def __init__(self, name):
        self.name = name

    def __del__(self):
        exit()

    def update(self):
        pass