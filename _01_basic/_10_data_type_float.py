"""
    10 数据类型-浮点数
"""
# 1 浮点数的表示
var_float_1 = 1.2
var_float_2 = 0.2
var_float_3 = .14  # 可以省略小数点前的 0
print(var_float_1, var_float_2, var_float_3)
# 科学计数法表示
var_float_4 = 5.12e2   # 5.12 乘以 10 的 2 次方
var_float_5 = 5.12e+2  # 5.12 乘以 10 的 2 次方(+ 号可以省略不写)
var_float_6 = 5.12E2  # 5.12 乘以 10 的 2 次方(e 可以写成 E)
var_float_7 = 5.12e-2  # 5.12 乘以 10 的 -2 次方
print(var_float_4, var_float_5, var_float_6, var_float_7)
print("====================================")


# 2 浮点数计算后，存在精度丢失，导致计算结果错误
var_error = 8.1 / 3  # 目标：8.1 / 3 = 2.7
print(var_error)     # 实际：2.6999999999999997

# 使用 Decimal 类计算，解决精度丢失问题
from decimal import Decimal
var_accurate = Decimal("8.1") / Decimal("3")
print(var_accurate)  # 2.7
