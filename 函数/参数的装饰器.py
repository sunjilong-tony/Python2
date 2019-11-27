# coding= utf-8


def wrapper(count):
    def inner(f):
        def demo(*args, **kwargs):
            for i in range(count):
                f(*args, **kwargs)
        return demo
    return inner


@wrapper(5)
def func():
    print("123456")

func()