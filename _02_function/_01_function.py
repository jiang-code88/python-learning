"""
    01 python 函数
     - 系统函数
        - 内置函数
        - 模块提供函数
     - 自定函数
     - 函数的调用方式
"""


# python 函数分为：系统函数、自定义函数
# 系统函数
# 1 内置函数
# 2 模块中提供的函数

# 自定义函数（使用 def 关键字，后跟函数名（函数标识符）与括号内的形参列表定义的函数）
# 函数的调用方式：函数名(实参列表)

def cal(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print(total)


cal(10)
print(cal(100))  # None 没有 return 返回值的函数调用默认返回 None
print(id(cal(100)))  # None 也是一种数据，也会分配内存空间存储该数据
# id() 函数是内置函数，可以返回对象/数据的内存地址


def get_sum(n1, n2):
    return n1 + n2


print(get_sum(2, 3))
