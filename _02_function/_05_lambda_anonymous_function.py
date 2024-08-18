"""
    05 函数作为参数传递-lambda 匿名函数
    匿名函数的特点：
     - 无需定义函数名称
     - 匿名函数只能使用一次
    匿名函数的基本语法：
     lambda 形参列表：函数体（一行代码）
     - lambda 关键字，表示定义匿名函数
     - 形参列表：表示接受的参数
     - 函数体：函数完成的功能，只能写一行代码，不能写多行代码，不需要 return
       一行代码执行的结果就是返回值
"""


def function(n1, n2, func):
    return func(n1, n2), n1 + n2


max_val, sum_val = function(2, 3,
                            lambda n1, n2: n1 if n1 > n2 else n2)
print(f"max_val={max_val}, sum_val={sum_val}")  # max_val=3, sum_val=5



