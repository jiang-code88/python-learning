"""
    04 函数作为参数传递
"""


def get_max_value(n1, n2):
    return n1 if n1 > n2 else n2


def function(n1, n2, func):
    """
    功能：调用 func 返回 n1 和 n2 的最大值，同时返回两数之和
    :param n1:
    :param n2:
    :param func:
    :return:
    """
    return func(n1, n2), n1 + n2


print(function(2, 3, get_max_value))  # (3, 5)

max_val, sum_val = function(10, -20, get_max_value)
print(f"max_val={max_val}, sum_val={sum_val}")  # max_val=10, sum_val=-10
