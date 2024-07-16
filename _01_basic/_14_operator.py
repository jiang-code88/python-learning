"""
    14 运算符
     - 算数运算符
     - 赋值运算符
     - 复合赋值运算符
        - python 特有简便变量交换方式
     - 比较运算符
     - 逻辑运算符
     - 三元运算符
     - 位运算符
"""
# 1  算术运算符 arithmetic
# +  加
# -  减
# *  乘
# /  除
# %  取模（取余）（取模运算原理：取模运算等同于公式 a % b = a - a // b * b，运算时要注意运算符的优先级）
print(10 % 3)  # 1
print(-10 % 3)  # 2
print(-10 % -3)  # -1
print(-10 % -3)  # -1
# // 取整除（向下取整，取结果小数约整偏向较小一方的数字）
print(9 // 2)  # 4.5
print(-9 // 2)  # -5
# ** 幂
print(2 ** 4)  # 2 的 4 次幂等于 16
print("=====================")

# 2 赋值运算符 assign
# 简单赋值运算符
# =
v1 = 10  # 10
print(v1)

# 复合赋值运算符
# +=
# v1 = v1 + 100
v1 += 100  # 110
print(v1)
# -=
# v1 = v1 - 20
v1 -= 20  # 90
print(v1)
# *=
# v1 = v1 * 10
v1 *= 10  # 900
print(v1)
# /=
# v1 = v1 / 2
v1 /= 2  # 450.0
print(v1)
# %=
# v1 = v1 % 7
v1 %= 7  # 2.0
print(v1)
# **=
# v1 = v1 ** 3
v1 **= 3  # 8.0
print(v1)
# //=
# v1 = v1 // 3
v1 //= 3  # 2.0
print(v1)

# 变量交换
x = 20
y = 30
print(f"没有交换前 x={x}, y={y}")
# 原始变量交换方式
# temp = x
# x = y
# y = temp
# python 中特有的简单变量交换方式
x, y = y, x
print(f"交换后 x={x}, y={y}")
print("=====================")

# 3 比较运算符 compare
# == 判断相等
# != 判断不想等
# <  判断小于
# >  判断大于
# <= 判断小于等于
# >= 判断大于等于
# is 判断两个变量引用对象是否为相同
# is not 判断两个变量引用对应是否不同
a = "str"
b = "str"
print(a is b)  # True 相同的对象
print(a is not b)  # False 不是不相同的对象
c = 1
d = 2
e = 1
print(c is d)  # False 不相同的对象
print(c is e)  # True 相同的对象
print("=====================")

# 4 逻辑运算符 logic
var1 = 10
var2 = 0
var3 = 20
# 布尔 "与"（and 是"短路运算符"，只有当第一个表达式为 True 时才去计算验证第二个表达式）
print(var1 and var2)  # 0 有假则假，返回 0 代表 False
print(var1 and var3)  # 20 双真为真，返回 and 右边表达式的值

# 布尔 "或"（or 是"短路运算符"，只有当第一个表达式为 False 时才去计算验证第二个表达式）
print(var1 or var3)  # 10 有真则真，返回为真的表达式值，双真时返回 or 左边表达式的值
print(var2 or var2)  # 0 双假为假，返回 0 代表 False

# 布尔 "非"
print(not var1)  # False
print(not var2)  # True
print("=====================")

# 5 三元运算符 ternary
k1 = 10
k2 = 80
maxK = k1 if k1 > k2 else k2  # 获取 k1 和 k2 的最大值
print(f"maxK={maxK}")

c1 = 10
c2 = 20
c3 = 30
maxC = (c1 if c1 > c2 else c2) if (c1 if c1 > c2 else c2) > c3 else c3
print(f"maxC={maxC}")


# 6 位运算符
