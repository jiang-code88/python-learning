"""
    13 数据类型转换
     - 隐式类型转换（自动类型转换）
     - 显示类型转换（强制类型转换）
"""
# 1 隐式类型转换（自动类型转换）
# 根据该变量使用的上下文（即变量的当前值），在运行时决定其数据类型
var1 = 10
print("var1 =", var1, "var1类型:", type(var1))  # int 类型
var1 = 1.1
print("var1 =", var1, "var1类型:", type(var1))  # float 类型
var1 = "hello"
print("var1 =", var1, "var1类型:", type(var1))  # str 类型

# 在运行时，数据类型会向高精度转换（例如 float 的精度高于 int，int 会向 float 转换）
var2 = 10           # int 类型
var3 = 1.2          # float 类型
var4 = var2 + var3  # 转换到 float 类型
print("var4 =", var4, "var4类型:", type(var4))
print("====================================")


# 2 显示类型转换（强制转换）
# 将数据类型作为函数名即可，对变量数据类型进行转换，
# 函数会返回一个新的对象/值，作为强制转换后的结果。
var5 = 10
var6 = float(var5)
var7 = str(var5)
var8 = int(var5)
print("var5 =", var5, "var5类型:", type(var5))
print("var6 =", var6, "var6类型:", type(var6))
print("var7 =", var7, "var7类型:", type(var7))
print("var8 =", var8, "var8类型:", type(var8))
print("====================================")

# 所有的对象（int，float）都可以使用 str() 函数转换为字符串。
# int 转 float 时，会增加小数部分，float 转 int 时，会直接去掉小数部分。

# 把字符串对象转换为 int，float 类型的数值类型数据
var9 = "123.45"
var10 = float(var9)
print("var9 =", var9, "var9类型:", type(var9))
print("var10 =", var10, "var10类型:", type(var10))

# 不能把 "hello" 转成一个整数，因为 "hello" 不符合浮点数格式，程序会报 ValueError 错误中止
var11 = "hello"
var12 = int(var11)

# 对一个变量进行强制转换，会返回一个数据/值（强制转换后，并不会影响原变量指向的数据/值的数据类型）
