# coding= utf-8


def singledemo(cls):
    instance = {}
    def inner(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return inner

#
# class Single(object):
#     instance1 = None
#     def __new__(cls, *args, **kwargs):
#         if cls.instance1 is None:
#             cls.instance1 = super().__new__(cls)
#         return cls.instance1
#
#