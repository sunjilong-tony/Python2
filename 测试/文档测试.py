# coding= utf-8
import doctest
def my(x, y):
    # doctest 严格按照python交互式命令的输入和输出来判断测试结果是否正确
    # 注意空格
    """
    >>> print(my(1,2))
    3
    """
    return x + y+1
doctest.testmod()