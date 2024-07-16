"""
    02 函数的注意事项
     - 同名函数，调用时的就近原则
     - 位置参数
     - 函数允许多个返回值
     - 关键字参数
     - 默认参数
     - 可变参数（不定长参数）
        - 0-N 个位置参数 *
        - 0-N 个关键字参数 **
     - 调用其他 py 文件（模块）函数
"""


# 1 如果同一文件中有多个同名自定义函数，调用函数时将遵循就近原则调用
def cry():
    print("cry()..hi..")


def cry():
    print("cry()..ok..")


# 该处函数调用将调用离此处最近的同名函数定义
cry()  # cry()..ok..
print("==============================")


# 2 位置参数：传递的实参和定义的形参顺序和个数必须一致，否则会报 TypeError 错误
def car_info(name, price, color):
    print(f"name->{name} price->{price} color->{color}")


car_info("Volvo", "250000", "blue")
print("==============================")


# 3 函数可以有多个返回值，返回值的数据类型不限
def fun(n1, n2):
    return n1 + n2, n1 - n2


result = fun(1, 2)
print(result)
r1, r2 = fun(1, 2)
print(r1, r2)
print("==============================")


# 4 关键字参数：函数调用时，可以通过 "形参名=实参名" 形式传递参数
# 关键字参数可以突破位置参数顺序和个数的限制
def book_info(title, author, price):
    print(f"title->{title} author->{author} price->{price}")


book_info("红楼梦", price="100", author="曹雪芹")
print("==============================")


# 5 函数支持默认参数（缺省参数）
# 定义函数时，可以给参数提供默认值；调用函数时，指定了实参，则以指定的为准，没有指定，则以默认值为准
# 默认参数需要连续的定义在参数末尾或全部参数都定义为默认参数，不允许间隔定义
def book_info_2(title='《thinking in python》', author='龟叔', price='19.9'):
    print(f"title->{title} author->{author} price->{price}")


book_info_2()
book_info_2("《thinking in Java》")
print("==============================")


# 6 函数支持可变参数（不定长参数）
# 应用场景：当调用函数时，不确定传入多少个实参的情况
# 传入的多个实参，会被组成一个元组（tuple）在函数内部使用
def sum_num(*args):  # * 代表 0-N 个位置参数
    print(f"args->{args}, args type->{type(args)}")
    total = 0
    for arg in args:
        total += arg
    return total


print(sum_num())
print(sum_num(1, 2, 3, 4, 5))
print("==============================")


# 7 函数的可变参数（不定长参数）还支持多个关键字参数，也就是调用时指定多个 "形参名=实参值" 传参
# 应用场景：当调用函数时，不确定传入多少个关键字参数的情况
# 传入的多个关键字参数，会被组成一个字典（dict）在函数内部使用
def person_info(**kwargs):  # ** 表示 0-N 个关键字参数
    print(f"kwargs->{kwargs} kwargs type->{type(kwargs)}")
    # 遍历 kwargs 字典，取出各个字典项的参数名
    for kwarg_name in kwargs:
        # kwargs[kwarg_name] 表示取出字典项的参数值
        print(f"{kwarg_name}->{kwargs[kwarg_name]}")


person_info()
person_info(name="john", age=23, sex="female", tel="1349882")

# 8 python 调用另外一个 .py 文件中的函数
# python 中一个文件就是一个模块
import _01_function  # 引入 _01_function.py 文件（即引入 _01_function 模块）

# 调用引入的 _01_function 模块的 get_sum() 函数
result = _01_function.get_sum(3, 4)
print(result)
