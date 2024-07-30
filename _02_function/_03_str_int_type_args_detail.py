"""
    03 字符串和数值类型变量的传参机制
     - 数值参数传参（值传递）
     - 字符串参数传参（值传递）
    结论：字符串和数值类型都是不可变数据类型，
         当对应的变量的值发生变化时，变量所对应的值的内存地址也会发生变化。
"""
# 数值参数的机制


def f1(num):
    print(f"计算前 f1() 函数，参数 num 的值：{num} 地址是：{id(num)}")  # 4326592320
    num += 1
    print(f"计算后 f1() 函数，参数 num 的值：{num} 地址是：{id(num)}")  # 4326592352
    return num


num = 10
print(f"调用 f1() 函数前，变量 num 的值：{num} 地址是：{id(num)}")  # 4326592320
re = f1(num)
print(f"调用 f1() 函数后，变量 num 的值：{num} 地址是：{id(num)}")  # 4326592320
print(f"调用 f1() 函数后，返回的变量值：{re} 地址是：{id(re)}")  # 4326592352
print("==============================================")


# 字符串参数的机制


def f2(name):
    print(f"计算前 f2() 函数，参数 name 的值：{name} 地址是：{id(name)}")  # 4311911712
    name += " hi"
    print(f"计算后 f2() 函数，参数 name 的值：{name} 地址是：{id(name)}")  # 4311891888
    return name


name = "jackson"
print(f"调用 f2() 函数前，变量 name 的值：{name} 地址是：{id(name)}")  # 4311911712
re = f2(name)
print(f"调用 f2() 函数后，变量 name 的值：{name} 地址是：{id(name)}")  # 4311911712
print(f"调用 f2() 函数后，返回的变量值：{re} 地址是：{id(re)}")  # 4311891888
print("===============================================")

